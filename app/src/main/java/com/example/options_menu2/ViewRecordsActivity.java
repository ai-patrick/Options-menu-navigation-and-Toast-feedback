package com.example.options_menu2;

import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import java.util.ArrayList;

public class ViewRecordsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_records);

        // Setup toolbar with back navigation
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
            getSupportActionBar().setDisplayShowHomeEnabled(true);
        }
        toolbar.setNavigationOnClickListener(v -> onBackPressed());

        // Read records from Intent
        TextView textViewRecords = findViewById(R.id.textViewRecords);
        ArrayList<String> records = getIntent().getStringArrayListExtra("records_list");

        if (records != null && !records.isEmpty()) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < records.size(); i++) {
                sb.append(i + 1).append(". ").append(records.get(i)).append("\n\n");
            }
            textViewRecords.setText(sb.toString());
        } else {
            textViewRecords.setText(getString(R.string.view_records_empty));
        }

        // Brief Toast on arrival
        Toast.makeText(this, R.string.toast_view_records, Toast.LENGTH_SHORT).show();
    }

    @Override
    public boolean onSupportNavigateUp() {
        onBackPressed();
        return true;
    }
}