package com.example.options_menu2;

import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    private static final String KEY_RECORDS = "records_list";
    private static final String KEY_DRAFT_NAME = "draft_name";
    private static final String KEY_DRAFT_REGNO = "draft_reg_no";

    // UI Components
    private TextInputLayout layoutStudentName;
    private TextInputLayout layoutRegNo;
    private TextInputEditText editStudentName;
    private TextInputEditText editRegNo;
    private TextView textDraftStatus;
    private TextView textRecordsCount;
    private Button buttonFaultDemo;

    // Data
    private ArrayList<String> recordsList = new ArrayList<>();
    private boolean hasUnsavedChanges = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        // Setup toolbar
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // Bind views
        layoutStudentName = findViewById(R.id.layoutStudentName);
        layoutRegNo = findViewById(R.id.layoutRegNo);
        editStudentName = findViewById(R.id.editStudentName);
        editRegNo = findViewById(R.id.editRegNo);
        textDraftStatus = findViewById(R.id.textDraftStatus);
        textRecordsCount = findViewById(R.id.textRecordsCount);
        buttonFaultDemo = findViewById(R.id.buttonFaultDemo);

        // Restore state if available
        if (savedInstanceState != null) {
            ArrayList<String> restored = savedInstanceState.getStringArrayList(KEY_RECORDS);
            if (restored != null) {
                recordsList = restored;
            }
            String draftName = savedInstanceState.getString(KEY_DRAFT_NAME);
            String draftRegNo = savedInstanceState.getString(KEY_DRAFT_REGNO);
            if (draftName != null) editStudentName.setText(draftName);
            if (draftRegNo != null) editRegNo.setText(draftRegNo);
        }

        updateRecordsCount();
        updateDraftStatus();

        // Text watchers to track unsaved changes
        TextWatcher watcher = new TextWatcher() {
            @Override public void beforeTextChanged(CharSequence s, int start, int count, int after) {}
            @Override public void onTextChanged(CharSequence s, int start, int before, int count) {
                hasUnsavedChanges = true;
                updateDraftStatus();
                // Clear errors when user starts typing
                layoutStudentName.setError(null);
                layoutRegNo.setError(null);
            }
            @Override public void afterTextChanged(Editable s) {}
        };
        editStudentName.addTextChangedListener(watcher);
        editRegNo.addTextChangedListener(watcher);

        // Fault demo button
        buttonFaultDemo.setOnClickListener(v -> demonstrateFault());
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.options_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int itemId = item.getItemId();

        if (itemId == R.id.action_add_record) {
            handleAddRecord();
            return true;
        } else if (itemId == R.id.action_view_records) {
            handleViewRecords();
            return true;
        } else if (itemId == R.id.action_about) {
            handleAbout();
            return true;
        } else {
            // Unknown/unhandled item - log warning and delegate safely
            Log.w(TAG, "Unhandled menu item selected: " + itemId + " (" + item.getTitle() + ")");
            return super.onOptionsItemSelected(item);
        }
    }

    private void handleAddRecord() {
        String name = editStudentName.getText() != null ? editStudentName.getText().toString().trim() : "";
        String regNo = editRegNo.getText() != null ? editRegNo.getText().toString().trim() : "";

        boolean valid = true;

        // Validate name
        if (name.isEmpty()) {
            layoutStudentName.setError(getString(R.string.error_name_required));
            valid = false;
        } else {
            layoutStudentName.setError(null);
        }

        // Validate registration number
        if (regNo.isEmpty()) {
            layoutRegNo.setError(getString(R.string.error_reg_no_required));
            valid = false;
        } else {
            layoutRegNo.setError(null);
        }

        if (!valid) {
            // Persistent validation errors shown via TextInputLayout.setError()
            // Do NOT use Toast for validation errors (requirement: keep visible long enough to act)
            return;
        }

        // Valid input - add record
        String record = name + " | " + regNo;
        recordsList.add(record);

        // Clear inputs
        editStudentName.setText("");
        editRegNo.setText("");
        hasUnsavedChanges = false;
        updateDraftStatus();
        updateRecordsCount();

        // Brief Toast confirmation without exposing sensitive personal data
        Toast.makeText(this, R.string.toast_add_record, Toast.LENGTH_SHORT).show();
    }

    private void handleViewRecords() {
        // Check for unsaved input
        String name = editStudentName.getText() != null ? editStudentName.getText().toString().trim() : "";
        String regNo = editRegNo.getText() != null ? editRegNo.getText().toString().trim() : "";

        if (!name.isEmpty() || !regNo.isEmpty()) {
            hasUnsavedChanges = true;
            // Show persistent AlertDialog warning before navigating
            new AlertDialog.Builder(this)
                    .setTitle(R.string.unsaved_title)
                    .setMessage(R.string.unsaved_message)
                    .setPositiveButton(R.string.discard_view, (dialog, which) -> {
                        hasUnsavedChanges = false;
                        editStudentName.setText("");
                        editRegNo.setText("");
                        updateDraftStatus();
                        navigateToViewRecords();
                    })
                    .setNegativeButton(R.string.stay_edit, null)
                    .show();
        } else {
            // No unsaved changes - proceed directly
            Toast.makeText(this, R.string.toast_view_records, Toast.LENGTH_SHORT).show();
            navigateToViewRecords();
        }
    }

    private void navigateToViewRecords() {
        Intent intent = new Intent(this, ViewRecordsActivity.class);
        intent.putStringArrayListExtra("records_list", recordsList);
        startActivity(intent);
    }

    private void handleAbout() {
        Toast.makeText(this, R.string.toast_about, Toast.LENGTH_SHORT).show();
        new AlertDialog.Builder(this)
                .setTitle(R.string.about_title)
                .setMessage(R.string.about_message)
                .setPositiveButton("OK", null)
                .show();
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        // Save records list to survive rotation
        outState.putStringArrayList(KEY_RECORDS, recordsList);
        // Save draft input
        outState.putString(KEY_DRAFT_NAME, editStudentName.getText() != null ? editStudentName.getText().toString() : "");
        outState.putString(KEY_DRAFT_REGNO, editRegNo.getText() != null ? editRegNo.getText().toString() : "");
    }

    private void updateRecordsCount() {
        textRecordsCount.setText(getString(R.string.records_saved_count, recordsList.size()));
    }

    private void updateDraftStatus() {
        if (hasUnsavedChanges) {
            textDraftStatus.setText(R.string.draft_status_unsaved);
            textDraftStatus.setTextColor(getColor(R.color.error_color));
        } else {
            textDraftStatus.setText(R.string.draft_status_clean);
            textDraftStatus.setTextColor(getColor(android.R.color.darker_gray));
        }
    }

    /**
     * Fault diagnosis demonstration: deliberately introduced fault
     * Shows symptom, cause (mismatched menu item ID), correction, and retest
     */
    public void demonstrateFault() {
        Log.d(TAG, "=== FAULT DEMONSTRATION START ===");
        Log.d(TAG, "Fault: Mismatched menu item ID in onOptionsItemSelected()");
        Log.d(TAG, "Symptom: Menu selection does nothing (no Toast, no navigation, no error)");
        Log.d(TAG, "Cause: Code checks for R.id.action_view_record (singular) but menu defines @+id/action_view_records (plural)");
        Log.d(TAG, "Correction: Use exact ID from menu resource: R.id.action_view_records");
        Log.d(TAG, "Retest: After fix, selection works correctly - Toast shows, navigation occurs");
        Log.d(TAG, "=== FAULT DEMONSTRATION END ===");

        new AlertDialog.Builder(this)
                .setTitle(R.string.fault_demo_title)
                .setMessage(R.string.fault_demo_message)
                .setPositiveButton("OK", null)
                .show();
    }
}