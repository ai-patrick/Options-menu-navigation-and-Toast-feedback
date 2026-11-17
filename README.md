# Options Menu Demo — ICS 2300 Lab 03 Homework 3

**Student:** Patrick Kilonzo Mbithi  
**Reg. Number:** SCT211-0036/2025  
**Course:** BSc Computer Science  
**Instructor:** Dr. Lawrence Nderu  
**Institution:** JKUAT  

---

## Overview

This Android application demonstrates the complete lifecycle of an Options Menu with three meaningful actions, proper event handling, user feedback via Toast and AlertDialog, inter-Activity navigation with correct Back button behavior, and a deliberate fault injection with full diagnosis.

**Package:** `com.example.options_menu`  
**Min SDK:** 24 (Android 7.0 Nougat)  
**Target SDK:** 36  
**Language:** Java 11  
**Theme:** `Theme.MaterialComponents.DayNight.DarkActionBar`

---

## Features Implemented

| Requirement | Implementation |
|-------------|----------------|
| **Options Menu** with ≥3 actions | `res/menu/options_menu.xml` — 4 items: Add Record, View Records, About, Toggle Fault Demo |
| **Stable item IDs** | `R.id.menu_add_record`, `R.id.menu_view_records`, `R.id.menu_about`, `R.id.menu_toggle_fault` |
| **Menu attached to screen** | `onCreateOptionsMenu()` inflates `R.menu.options_menu` |
| **Toast feedback** | Brief non-critical messages for Add Record, View Records, About |
| **AlertDialog for rich content** | About dialog + Fault explanation dialog (multi-line, persistent) |
| **Validation errors visible** | Fault explanation uses AlertDialog (not Toast) so user can read fully |
| **Screen change action** | "View Records" → `startActivity(RecordsActivity.class)` |
| **Back navigation without duplicate** | `onPause`/`onResume` cycle; `onCreate` not re-run; no `onNewIntent` |
| **Deliberate fault** | `demonstrateFault` flag swaps `effectiveItemId` to wrong constant |
| **Fault diagnosis** | Symptom, cause, correction, retest documented |
| **State preservation** | `onSaveInstanceState`/`onCreate` persist & restore fault flag |

---

## Project Structure

```
Options_menu/
├── app/
│   ├── src/main/
│   │   ├── java/com/example/options_menu/
│   │   │   ├── MainActivity.java       ← Menu, toasts, navigation, fault demo
│   │   │   ├── RecordsActivity.java    ← Second screen: ListView of records
│   │   │   └── RecordManager.java      ← Singleton in-memory record storage
│   │   ├── res/
│   │   │   ├── layout/
│   │   │   │   ├── activity_main.xml      ← Main UI with instructions + fault toggle
│   │   │   │   └── activity_records.xml   ← ListView + empty state
│   │   │   ├── menu/
│   │   │   │   └── options_menu.xml       ← 4 menu items with stable IDs
│   │   │   ├── values/
│   │   │   │   ├── strings.xml            ← All user-facing text
│   │   │   │   └── themes.xml             ← MaterialComponents theme
│   │   │   └── AndroidManifest.xml        ← Declares both activities, parent link
│   │   └── build.gradle.kts
│   ├── build.gradle.kts
│   ├── settings.gradle.kts
│   └── gradle/
└── README.md
```

---

## Menu Resource

**File:** `app/src/main/res/menu/options_menu.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <item
        android:id="@+id/menu_add_record"
        android:title="@string/menu_add_record"
        android:icon="@android:drawable/ic_menu_add"
        app:showAsAction="ifRoom|withText" />

    <item
        android:id="@+id/menu_view_records"
        android:title="@string/menu_view_records"
        android:icon="@android:drawable/ic_menu_view"
        app:showAsAction="ifRoom|withText" />

    <item
        android:id="@+id/menu_about"
        android:title="@string/menu_about"
        android:icon="@android:drawable/ic_menu_info_details"
        app:showAsAction="never" />

    <item
        android:id="@+id/menu_toggle_fault"
        android:title="@string/menu_toggle_fault"
        android:icon="@android:drawable/ic_menu_manage"
        app:showAsAction="never" />

</menu>
```

**How it's attached:** In `MainActivity.onCreateOptionsMenu()`:
```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    getMenuInflater().inflate(R.menu.options_menu, menu);
    return true;
}
```

---

## Event Handling

### Menu Selection Routing (`onOptionsItemSelected`)

```java
@Override
public boolean onOptionsItemSelected(MenuItem item) {
    int itemId = item.getItemId();
    
    // Fault injection: only for the 3 assessed actions
    int effectiveItemId = demonstrateFault ? R.id.menu_view_records : itemId;

    if (effectiveItemId == R.id.menu_add_record) {
        handleAddRecord();
        return true;
    } else if (effectiveItemId == R.id.menu_view_records) {
        handleViewRecords();
        return true;
    } else if (effectiveItemId == R.id.menu_about) {
        handleAbout();
        return true;
    } else if (itemId == R.id.menu_toggle_fault) {
        // ALWAYS uses real itemId — user can always turn fault off
        onToggleFaultClick(null);
        return true;
    }
    // Safe fallback
    Toast.makeText(this, "Unknown action", Toast.LENGTH_SHORT).show();
    return super.onOptionsItemSelected(item);
}
```

### Action Handlers

| Action | Feedback | Behavior |
|--------|----------|----------|
| **Add Record** | `Toast.LENGTH_SHORT` (`toast_record_added`) | Adds timestamped record to `RecordManager` singleton |
| **View Records** | `Toast.LENGTH_SHORT` (`toast_view_records`) | Launches `RecordsActivity` via explicit `Intent` |
| **About** | `Toast` + `AlertDialog` | Shows app info in modal dialog |
| **Toggle Fault** | `Toast.LENGTH_LONG` + status UI update | Flips `demonstrateFault` flag; shows explanation when enabled |

---

## Screen Navigation & Back Handling

**Event Path for "View Records":**
1. User taps ⋮ → selects "View Records"
2. `onOptionsItemSelected()` matches `R.id.menu_view_records`
3. `handleViewRecords()` called → shows Toast → `startActivity(RecordsActivity.class)`
4. `RecordsActivity.onCreate()` loads records from `RecordManager`
5. User presses **BACK** → `RecordsActivity.finish()` → returns to `MainActivity`
6. `MainActivity.onResume()` fires — **NO duplicate action** because:
   - `MainActivity` was paused, not destroyed
   - `onCreate()` NOT called again
   - No `onNewIntent()` override exists

---

## Deliberate Fault Demonstration

| Aspect | Details |
|--------|---------|
| **Fault** | In `onOptionsItemSelected()`, when `demonstrateFault=true`, `effectiveItemId` is set to `R.id.menu_view_records` instead of actual `itemId` |
| **Symptom** | Selecting "Add Record" shows "Opening records list…" Toast (View Records message) instead of "Record added" |
| **Cause** | If-chain matches wrong branch — View Records handler executes for ALL selections |
| **Correction** | Toggle fault OFF (button or menu) → `effectiveItemId = itemId` restored |
| **Retest** | All three actions route correctly; rotation preserves state via `onSaveInstanceState` |

**Why `menu_toggle_fault` is immune:** It's checked against real `itemId` (line 99), so the control to disable the fault always works.

---

## State Preservation

```java
@Override
protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    outState.putBoolean("demonstrateFault", demonstrateFault);
}

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    if (savedInstanceState != null) {
        demonstrateFault = savedInstanceState.getBoolean("demonstrateFault", false);
    }
}
```

---

## Build & Run

```bash
# From project root
./gradlew assembleDebug

# Install on connected device/emulator
./gradlew installDebug
```

Or open in Android Studio → **Run ▶**

---

## Documentation

- **HTML Walkthrough:** `Lab_03_hm3_Options_Menu_Walkthrough.html` — Interactive, print-ready (matches form_input_app_walkthrough.html style)
- **PDF Report:** `Lab_03_hm3_Mbithi_SCT211-0036_2025.pdf` — 32-page formal submission

---

## Related Repository

Reference implementation: [Kiamapatrick/Options_menu](https://github.com/Kiamapatrick/Options_menu.git)

---

## License

Academic submission for ICS 2300 — Mobile Application Development. Submitted privately to instructor via Piazza Q&A.