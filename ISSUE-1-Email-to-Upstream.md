# Issue #1: Email sent to Upstream Developer
**Status:** Closed
**Date:** 2026-09-20

This issue tracks the email sent to the upstream developer (kusik) explaining the phone port modifications.

---
**Subject:** Porting Wrist Chess to Android Phones - Code & Details

Hi kusik,

I love Wrist Chess, but I really wanted to play it natively on my Android phone (a Unihertz Titan 2 Elite) instead of just on my watch. Since the Play Store restricts it to Wear OS devices and only ships 32-bit (armeabi-v7a) libraries, I spent some time extracting the APK, building the missing 64-bit engine libraries, and creating a few shims so it runs perfectly on regular phones.

I thought you might be interested in seeing the changes required, in case you ever want to publish a "phone" flavor or make the app universal. 

Here is what I did:
1. Manifest Changes: I made the `com.google.android.wearable` library and the `android.hardware.type.watch` feature optional, and removed the strict split-APK requirements.
2. 64-bit Support: I built Fairy-Stockfish for `arm64-v8a` and grabbed the 64-bit versions of Firebase/AndroidX from Maven, so the app can install on modern 64-bit-only phones like the Pixel 7+ and Titan 2 Elite.
3. UI Adjustments: I modified the board sizing to use `smallestScreenWidthDp - 100` instead of a hardcoded dimension so it fills phone screens nicely without cutting off player names. I also scaled the Puzzles screen text to prevent clipping.
4. Wear SDK Stubs: I added a simple stub for `com.google.wear.Sdk$VERSION.WEAR_SDK_INT` and the ambient delegates, since those classes are absent on non-wearable Android 14+ devices and cause NoClassDefFoundErrors.
5. REMOTE_INPUT Fix: I added an exported `RemoteInputActivity` to handle the intent used for entering the Lichess API token, since the implicit wearable intent doesn't resolve natively on phones.

I’ve uploaded all the build scripts, the `arm64-v8a` prebuilt libraries, and the exact smali patches to my GitHub repository. You can find all the code and instructions here:
[Insert GitHub Repo URL here]

Feel free to use any of this code if you ever decide to officially support phones. Let me know if you have any questions!

Best,
Daniel
