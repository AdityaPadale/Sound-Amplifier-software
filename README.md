 # 🎙️ Real-Time Audio Amplifier

A simple Python project that captures audio from your microphone, amplifies it in real-time, and plays it back through your speakers. Built using **PyAudio** and **NumPy**.

---

## 🚀 Features
- Real-time audio capture and playback  
- Adjustable **amplification factor**  
- Works with most microphones and speakers  
- Simple and lightweight (GUI and CLI)  

---

## 📦 Requirements
Make sure you have the following installed:

- Python 3.8+  
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)  
- NumPy  

---

⚠️ On some systems, you may need to install PortAudio before PyAudio.

🪟 Windows Setup
1) Install Python dependencies

Try the direct install first:
```bash
pip install numpy pyaudio
```
If PyAudio fails to build, use a precompiled wheel via pipwin:
```bash
pip install pipwin
pipwin install pyaudio
```
2) Verify microphone & speaker access

Ensure your Input and Output devices are enabled in Windows Sound Settings.

Headphones recommended to avoid feedback sound loops.


If multiple devices exist, see 🔧 Advanced: Selecting Devices below.

---

▶️ Usage

Run the amplifier script from the project root:
```bash
python amplifier.py
```
You should see:

Sound Amplifier Running... Press Ctrl+C to stop.

⏸️ Press Ctrl+C to stop.

---

⚙️ Parameter	Default	Description:
- CHUNK	1024	Number of audio samples per frame
- FORMAT	pyaudio.paInt16	Audio format (16‑bit)
- AMPLIFICATION_FACTOR	3.0	Multiplier for volume (higher ⇒ louder)

---
⚠️ Caution: Very high AMPLIFICATION_FACTOR can cause distortion and may damage speakers or ears. Start low, increase gradually and keep your device away from any of the frequency to reduce wavy surrounding sound. ⚡

