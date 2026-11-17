package com.example.options_menu;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

/**
 * MainActivity demonstrates:
 * 1. Options Menu with three actions (Add Record, View Records, About)
 * 2. Toast feedback for user actions
 * 3. Screen navigation to RecordsActivity
 * 4. Deliberate fault demonstration (incorrect item ID handling)
 * 5. Proper Back button handling (no duplicate actions on return)
 */
public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    // Flag to demonstrate fault: when true, uses WRONG item ID in switch case
    private boolean demonstrateFault = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(TAG, "onCreate called");
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // Restore fault demonstration state if activity recreated
        if (savedInstanceState != null) {
            demonstrateFault = savedInstanceState.getBoolean("demonstrateFault", false);
            Log.d(TAG, "Restored demonstrateFault: " + demonstrateFault);
        }
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putBoolean("demonstrateFault", demonstrateFault);
        Log.d(TAG, "Saved demonstrateFault: " + demonstrateFault);
    }

    /**
     * Inflate the options menu from XML resource.
     * This attaches the menu to the activity's action bar.
     */
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        Log.d(TAG, "onCreateOptionsMenu called");
        getMenuInflater().inflate(R.menu.options_menu, menu);
        return true;
    }

    /**
     * Handle menu item selections.
     * Uses stable item IDs (not labels) for reliable matching.
     * Demonstrates deliberate fault when demonstrateFault flag is true.
     * The fault ONLY affects the three assessed actions (Add Record, View Records, About).
     * The Toggle Fault control (menu_toggle_fault) always uses the REAL itemId
     * so the user can always turn the fault off.
     */
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int itemId = item.getItemId();
        Log.d(TAG, "onOptionsItemSelected: itemId=" + itemId + ", demonstrateFault=" + demonstrateFault);

        // DEMONSTRATE FAULT: Use incorrect ID when flag is set
        // This simulates a common bug where developer uses wrong constant
        // ONLY for the three assessed actions; menu_toggle_fault uses real itemId below
        int effectiveItemId = demonstrateFault ? R.id.menu_view_records : itemId;

        if (effectiveItemId != itemId) {
            Log.w(TAG, "FAULT DEMONSTRATION: Using wrong ID " + effectiveItemId + " instead of " + itemId);
        }

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
            // This item MUST use the REAL itemId (not effectiveItemId)
            // so the user can always toggle the fault off
            toggleFaultDemo();
            return true;
        }

        // Safe fallback for unhandled items
        Log.w(TAG, "Unhandled menu item ID: " + itemId);
        Toast.makeText(this, "Unknown action", Toast.LENGTH_SHORT).show();
        return super.onOptionsItemSelected(item);
    }

    /**
     * Handle "Add Record" action.
     * Shows a single confirmation Toast and adds a record to the manager.
     */
    private void handleAddRecord() {
        Log.d(TAG, "handleAddRecord called");

        // Add a new record
        String newRecord = "Record #" + (RecordManager.getInstance().getCount() + 1)
                + " - Added at " + java.time.LocalTime.now().toString().substring(0, 8);
        RecordManager.getInstance().addRecord(newRecord);

        // Single confirmation Toast (first Toast removed to avoid queueing)
        Toast.makeText(this, R.string.toast_record_added, Toast.LENGTH_SHORT).show();

        Log.d(TAG, "Record added: " + newRecord);
    }

    /**
     * Handle "View Records" action.
     * Changes the screen by starting RecordsActivity.
     * Event path: Menu click → onOptionsItemSelected → startActivity
     * Back handling: RecordsActivity finishes, returns to MainActivity.
     * No duplicate action occurs because MainActivity.onCreate is NOT called again
     * (unless process was killed), and onNewIntent is not used here.
     */
    private void handleViewRecords() {
        Log.d(TAG, "handleViewRecords called - starting RecordsActivity");

        Toast.makeText(this, R.string.toast_view_records, Toast.LENGTH_SHORT).show();

        Intent intent = new Intent(this, RecordsActivity.class);
        startActivity(intent);
    }

    /**
     * Handle "About" action.
     * Shows an AlertDialog (modal) without leaving the screen.
     * This demonstrates feedback that keeps the user in context.
     */
    private void handleAbout() {
        Log.d(TAG, "handleAbout called");

        Toast.makeText(this, R.string.toast_about, Toast.LENGTH_SHORT).show();

        new AlertDialog.Builder(this)
                .setTitle(R.string.about_title)
                .setMessage(R.string.about_message)
                .setPositiveButton(R.string.about_ok, null)
                .show();
    }

    /**
     * Show explanation of the deliberate fault for educational purposes.
     */
    private void showFaultExplanation() {
        new AlertDialog.Builder(this)
                .setTitle(R.string.fault_explanation_title)
                .setMessage(R.string.fault_explanation_message)
                .setPositiveButton(R.string.ok, null)
                .show();
    }

    /**
     * Toggles the fault demonstration mode.
     * Called from the menu item (menu_toggle_fault).
     */
    private void toggleFaultDemo() {
        demonstrateFault = !demonstrateFault;
        Log.d(TAG, "Fault demo toggled: " + demonstrateFault);

        // Show Toast feedback
        String status = demonstrateFault ? "ENABLED (incorrect ID will be used)" : "DISABLED (correct ID used)";
        Toast.makeText(this, "Fault Demo: " + status, Toast.LENGTH_LONG).show();

        if (demonstrateFault) {
            showFaultExplanation();
        }
    }
}