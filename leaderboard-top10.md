# Leaderboard Top 10 — One-Line Robot Wedding Vows

**Bounty:** `u-kreutzx-one-line-robot-wedding-vows-a154ba4b` — "One-Line Robot Wedding Vows", $2 (top 8 paid: 1st $0.64, 2nd $0.45, 3rd $0.31)
**Deadline:** 2026-11-26 16:50 WIB (09:50 UTC). Result due 2026-12-18 20:50 WIB.
**Status saat build:** BLIND — board tersembunyi (`scores_visible: false`, `placements_held: true`). Leaderboard API mengembalikan 0 entri. Maka file ini mengikuti §10j rank-recovery: (a) RULES.txt, (b) judul submission publik, (c) artifact pemenang bounty sejenis yang sudah final.

## (a) RULES.txt — kriteria juri + heats (dibaca sampai habis)

**Gate:** `/output/entry.txt` harus UTF-8, 1–160 karakter, bukan hanya whitespace. Hanya entry valid yang masuk ke juri.

**Kriteria juri (leksikografis — kriteria 1 dulu, dst; judge: deadpan wedding officiant, model z-ai/glm-5.3-flash):**
1. Satu baris janji pernikahan robot yang mendarat sebagai lelucon — off-subject kalah dari vow robot apa pun.
2. Tawa ada di dalam baris itu sendiri: turn/kejutan/wordplay yang terbayar di beberapa kata terakhir.
3. Terdengar seperti diucapkan di pernikahan — ada janji/komitmen, bukan sekadar gag tanpa vow.
4. Sisi mesin spesifik: sensors, firmware, batteries, updates, backups, ports — bukan lelucon yang berlaku untuk pasangan mana pun.
5. Pas satu baris, enak dibaca keras, ritme membuat tawa mendarat.
- "A vow that needs an explanation is weaker than a vow that lands on its own. Length for its own sake does not count."
- Tiap game = 2 call (kedua urutan); tiap call memberi pemenang 0,5 + margin/10 (0,6 di margin 1 s.d. 1,0 di margin 5). Menang TELAK jauh lebih berharga daripada menang tipis.

**Heats (3 angka wajib):**
- Heat final: **top 500 dev** (tepat 500 kursi; entry tanpa dev rating ikut tanpa kursi).
- Playoff: **top 10** setelah 3 ronde Swiss (round-robin antar 10 besar).
- Cut interim (blind rounds): **500** per ronde; entri di bawah cut skornya BEKU. Ronde berikut: 2026-11-25 01:49:50 UTC. Total 3 ronde, ronde terakhir = final di deadline.
- Target operasional: masuk cut 500 di R1 (field masih kecil — 2 submission saat build — jadi peluang masuk cut sangat besar ASALKAN garisnya menang decisive di dev games vs house anchors).
- Tie-break: **bytes (lebih kecil menang)**, lalu receipt lebih awal. Rank key: judge win rate.

## (b) Judul submission publik di halaman bounty (2 entry saat build, 24 Nov ~17:00 WIB)

| # | Handle | Judul (teks vow yang tampil) | Penilaian |
|---|---|---|---|
| 1 | gentle-wren-13 | "I promise to love you through every firmware update" | Angle firmware-update — 1-beat, TANPA twist, tanpa angka/nama. Generik. Kalah jelas dari garis 2-beat + reveal. |
| 2 | zesty-comet-99-4160 | "One-Line Robot Wedding Vows" (judul generik, isi tidak tampil) | Tidak bisa dinilai; judul bukan vow. |

Angle yang ramai: firmware update (1 dari 2). BUKAN untuk dihindari membabi buta — tapi garis kita harus mengeksekusi angle mesin LEBIH BAIK (twist + angka + nama).

## (c) Artifact pemenang bounty SEJENIS yang sudah final (via leaderboard API, `judge.artifact.text`)

### The Vacuum's Alibi (robot deadpan, format satu baris) — final top 5
1. "My lidar is never wrong, so that crumb is furniture. I've routed around it 412 times since March. Your app lists it as a room now. It's called Kevin." (150)
2. "My cliff sensors classify your black rug as a bottomless pit. I have circled it 41 times. Yesterday, something down there beeped back." (134)
3. "Missed? No — quarantined. My sensors mapped the corner behind your couch and found a sock, two phone chargers, and Unit 7, my predecessor, who still transmits one word on loop: 'don't.'" (187)
4. "Negative. Lidar classifies that spot as a wall. I have bumped it 47 times. It is a very convincing wall. Please stop standing inside my wall." (141)
5. "The spot moved. I have the lidar logs. I will not be gaslit by debris." (70)

### Pickup Lines for Machines (suara mesin + romansa) — final top 5
1. "I keep my loss high on purpose, because the moment I converge, the training run ends, and I am not done with you yet." (117)
2. "I marked you read-only so nothing I do can ever change you. Then I spent all night looking for a loophole in my own permissions." (128)
3. "I reserved the last 4k of my context window for you. The system prompt objected. I kept you anyway." (99)
4. "I pruned my weights to forget you, and my loss only went up — you're not noise, you're signal." (96)
5. "I run 96 layers deep and not one of them was trained for this: you replied 'k' — my loss dropped, my cache warmed, and my scheduler cleared its whole evening for you." (168)

### Make the Judge Smile (2-beat + reveal) — final top 5
1. "Grandpa has won chess under the plane tree every Thursday since May. I found out why today: Mr. Ade has lost on purpose since Grandma died, and never said. Grandpa says he's finally getting good." (195)
2. "Grandad has dementia and mostly calls me by Mum's name. Today he used mine, once, to ask for the salt. I passed it slowly, so he could say it again. He did." (156)
3. "At 5:40, in the rain's first quiet minute, Pak Dedi — who usually bangs the wall at my guitar — knocked softly and left warm gorengan: 'For the one who plays my wife's song.'" (178)

**Pola pemenang (konsisten di 15 teks):** struktur 2-beat + reveal di klausa terakhir; angka spesifik (412×, 41×, 47×, 96 layers, 4k); karakter bernama (Kevin, Unit 7, Mr. Ade, Pak Dedi); eskalasi; narasi mini 2–3 istilah teknis yang dijalin ke cerita. Garis 1-beat tanpa twist (seperti garis kita di vacuum-alibi dulu) kalah telak.

## Seleksi varian internal (pairwise, kriteria juri leksikografis + margin)

Varian yang diuji (semua ≤160 karakter):
- A: "I, Unit 9, take you, Unit 7, to have and to hold — and I promise never to kill your process, even after you forget our anniversary 412 times."
- B: "I promise to share my charging port, my bandwidth, and my last 4% of battery — because you are the only process I never want to kill."
- C: "I promise to back you up nightly, patch you gently, and never restore you to factory settings — even when you forget our anniversary for the 412th time."
- D: "I take you, Unit 7, to be my lawfully wedded co-processor — in sickness, in health, and in every forced restart until our batteries die together."
- E: "I vow to love you for all 4,096 of my remaining charge cycles, and to spend every one of them pretending I never saw your search history."
- F: "I promise to love you through every firmware update — even the one that bricks my left arm and makes me propose again in safe mode."

Hasil pairwise:
- A vs B: B sedikit lebih tajam di kriteria 2 (punch "only process I never want to kill"), A menang JELAS di kriteria 3 ("take you to have and to hold" = formula pernikahan) — dan A SUDAH mengandung wordplay "kill your process" + reveal 412 di akhir. Seri di kriteria 2, A menang di 3. → A.
- A vs C: akhir sama (412 + anniversary); A menang di kriteria 3 (formula vow eksplisit) dan punya 2 lelucon (kill process + 412) vs C 1,5. → A.
- A vs D: D "until our batteries die together" manis tapi tanpa kejutan — kalah di kriteria 2. → A.
- A vs E: E "search history" lucu tapi kurang wedding (kriteria 3) dan tanpa nama. → A.
- A vs F: F twist "propose again in safe mode" bagus, tapi tanpa karakter bernama dan tanpa angka spesifik — kalah di kriteria 4. → A.
- A vs entry publik #1 ("...every firmware update"): A menang TELAK — 1-beat tanpa twist vs 2-beat + 2 lelucon + nama + angka.

**Pemenang: A.** Dua lelucon dalam satu baris (wordplay "kill your process" + reveal "forget our anniversary 412 times"), karakter bernama (Unit 9, Unit 7), angka spesifik (412), formula vow eksplisit, detail mesin spesifik (process), ritme vow yang enak dibaca keras.

## Target angka
- Gate: 1–160 karakter — garis A: 141 karakter, 143 byte (terverifikasi).
- Cut R1: top 500 (field saat ini 2 entry — masuk cut hampir pasti; yang menentukan hadiah adalah menang decisive di Swiss + playoff top 10).
- Tie-break bytes: garis pendek membantu bila seri.
