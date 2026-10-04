import os
import tempfile
import io
import librosa
import numpy as np
import streamlit as st
from resemblyzer import VoiceEncoder, preprocess_wav

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()

def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()
        
        # Write bytes to a temporary OS file so librosa can decode browser audio formats safely
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_bytes)
            tmp_file_path = tmp_file.name

        try:
            # Read from the file path instead of BytesIO
            audio, sr = librosa.load(tmp_file_path, sr=16000)
            wav = preprocess_wav(audio)
            embedding = encoder.embed_utterance(wav)
            return embedding.tolist()
        finally:
            # Always delete the temporary file after extraction
            if os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)

    except Exception as e:
        st.error(f'Voice recognition error: {e}')
        return None

def identify_speaker(new_embedding, candidate_dict, threshold=0.65):
    if new_embedding is None or not candidate_dict:
        return None, 0.0
        
    best_sid = None
    best_score = -1.0
    
    # Ensure numpy array for dot product
    new_emb_np = np.array(new_embedding)

    for sid, stored_embedding in candidate_dict.items():
        if stored_embedding:
            stored_emb_np = np.array(stored_embedding)
            similarity = np.dot(new_emb_np, stored_emb_np)
            
            if similarity > best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid, best_score

    return None, best_score

def process_bulk_audio(audio_bytes, candidate_dict, threshold=0.65):
    try:
        encoder = load_voice_encoder()
        
        # Write bytes to temp file for librosa
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_bytes)
            tmp_file_path = tmp_file.name
            
        try:
            audio, sr = librosa.load(tmp_file_path, sr=16000)
        finally:
            if os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)

        segments = librosa.effects.split(audio, top_db=30)
        identify_results = {}

        for start, end in segments:
            # Skip segments shorter than 0.5 seconds
            if (end - start) < sr * 0.5:
                continue
                
            segments_audio = audio[start:end]
            wav = preprocess_wav(segments_audio)
            embedding = encoder.embed_utterance(wav)

            sid, score = identify_speaker(embedding.tolist(), candidate_dict, threshold)

            if sid:
                # Check dictionary, not function name
                if sid not in identify_results or score > identify_results[sid]:
                    identify_results[sid] = score
                    
        return identify_results
        
    except Exception as e:
        st.error(f'Bulk process error: {e}')
        return {}