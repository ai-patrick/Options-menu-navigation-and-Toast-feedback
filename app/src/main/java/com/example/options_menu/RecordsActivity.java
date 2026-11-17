package com.example.options_menu;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.ArrayList;
import java.util.List;

/**
 * RecordsActivity displays the list of stored records.
 * Demonstrates screen change from MainActivity and proper Back navigation.
 */
public class RecordsActivity extends AppCompatActivity {

    private static final String TAG = "RecordsActivity";

    private ListView listViewRecords;
    private TextView textViewEmpty;
    private ArrayAdapter<String> recordsAdapter;
    private List<String> recordsList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(TAG, "onCreate called");
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_records);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.records_main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // Initialize views
        listViewRecords = findViewById(R.id.listViewRecords);
        textViewEmpty = findViewById(R.id.textViewEmpty);

        // Initialize data
        recordsList = RecordManager.getInstance().getRecords();
        recordsAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, recordsList);
        listViewRecords.setAdapter(recordsAdapter);

        // Show/hide empty state
        updateEmptyState();

        // Set item click listener
        listViewRecords.setOnItemClickListener((parent, view, position, id) -> {
            String record = recordsList.get(position);
            Toast.makeText(this, "Selected: " + record, Toast.LENGTH_SHORT).show();
        });

        Log.d(TAG, "RecordsActivity initialized with " + recordsList.size() + " records");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d(TAG, "onResume called");
        // Refresh data in case records were added
        refreshRecords();
    }

    private void refreshRecords() {
        recordsList.clear();
        recordsList.addAll(RecordManager.getInstance().getRecords());
        recordsAdapter.notifyDataSetChanged();
        updateEmptyState();
    }

    private void updateEmptyState() {
        if (recordsList.isEmpty()) {
            listViewRecords.setVisibility(View.GONE);
            textViewEmpty.setVisibility(View.VISIBLE);
        } else {
            listViewRecords.setVisibility(View.VISIBLE);
            textViewEmpty.setVisibility(View.GONE);
        }
    }
}