package com.example.options_menu;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

/**
 * Singleton manager for storing and retrieving records.
 * In a real app, this would use Room database or SharedPreferences.
 */
public class RecordManager {

    private static RecordManager instance;
    private final List<String> records;

    private RecordManager() {
        records = new ArrayList<>();
        // Add some sample records for demonstration
        addSampleRecords();
    }

    public static synchronized RecordManager getInstance() {
        if (instance == null) {
            instance = new RecordManager();
        }
        return instance;
    }

    private void addSampleRecords() {
        records.add("Sample Record 1 - " + UUID.randomUUID().toString().substring(0, 8));
        records.add("Sample Record 2 - " + UUID.randomUUID().toString().substring(0, 8));
    }

    public List<String> getRecords() {
        return new ArrayList<>(records); // Return copy to prevent external modification
    }

    public void addRecord(String record) {
        records.add(record);
    }

    public void clearAll() {
        records.clear();
    }

    public int getCount() {
        return records.size();
    }
}