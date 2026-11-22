"""
워디 챌린지 발음 mp3 만들기 (구글 클라우드 TTS)
- tools/audio-needed.json 에 있는 문장·단어를 여성(f)·남성(m) 두 목소리로 만들어
  audio/f/aXXXX.mp3, audio/m/aXXXX.mp3 에 저장하고 audio/manifest.json 에 등록해요.
- 이미 등록된 문장은 건너뛰어요. 저장소 맨 위 폴더에서 실행하세요.

준비 (한 번만):
  pip install google-cloud-texttospeech
  구글 클라우드 콘솔에서 Text-to-Speech API 사용 설정 → 서비스 계정 키(JSON) 받기
  export GOOGLE_APPLICATION_CREDENTIALS=/경로/키.json      (윈도우: set GOOGLE_APPLICATION_CREDENTIALS=...)
실행:
  python tools/make_audio.py
"""
import json, os
from google.cloud import texttospeech as tts

# 기존 워디 mp3와 같은 목소리를 쓰셨다면 이름을 그걸로 바꿔 주세요
VOICES = {"f": "en-US-Neural2-F", "m": "en-US-Neural2-J"}

def main():
    man_path = "audio/manifest.json"
    man = json.load(open(man_path, encoding="utf-8"))
    items = man["items"]
    need = [t for t in json.load(open("tools/audio-needed.json", encoding="utf-8")) if t not in items]
    nums = [int(v[1:]) for v in items.values() if v[1:].isdigit()]
    n = max(nums) if nums else 0
    client = tts.TextToSpeechClient()
    for k in VOICES: os.makedirs(f"audio/{k}", exist_ok=True)
    for text in need:
        n += 1; aid = f"a{n:04d}"
        # 단어 하나는 끝이 툭 끊기지 않게 마침표를 붙여 자연스럽게 읽혀요
        say = text if text[-1:] in ".!?" else text + "."
        for k, voice in VOICES.items():
            res = client.synthesize_speech(
                input=tts.SynthesisInput(text=say),
                voice=tts.VoiceSelectionParams(language_code="en-US", name=voice),
                audio_config=tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3, speaking_rate=0.95),
            )
            open(f"audio/{k}/{aid}.mp3", "wb").write(res.audio_content)
        items[text] = aid
        print(aid, text)
    json.dump(man, open(man_path, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"완료: {len(need)}개 추가")

if __name__ == "__main__":
    main()
