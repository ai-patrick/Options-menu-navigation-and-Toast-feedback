#!/usr/bin/env python3
"""
Generate PDF documentation for the Options Menu Demo app.
Follows the structure and style of form_input_application.html.
"""

from fpdf import FPDF
import os

class LabReportPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        # Add Unicode fonts (Liberation Sans/Mono)
        self.add_font('Liberation', '', '/usr/share/fonts/liberation/LiberationSans-Regular.ttf', uni=True)
        self.add_font('Liberation', 'B', '/usr/share/fonts/liberation/LiberationSans-Bold.ttf', uni=True)
        self.add_font('Liberation', 'I', '/usr/share/fonts/liberation/LiberationSans-Italic.ttf', uni=True)
        self.add_font('Liberation', 'BI', '/usr/share/fonts/liberation/LiberationSans-BoldItalic.ttf', uni=True)
        self.add_font('LiberationMono', '', '/usr/share/fonts/liberation/LiberationMono-Regular.ttf', uni=True)
        self.add_font('LiberationMono', 'B', '/usr/share/fonts/liberation/LiberationMono-Bold.ttf', uni=True)
        self.add_font('LiberationMono', 'I', '/usr/share/fonts/liberation/LiberationMono-Italic.ttf', uni=True)
        self.add_font('LiberationMono', 'BI', '/usr/share/fonts/liberation/LiberationMono-BoldItalic.ttf', uni=True)
        
    def header(self):
        if self.page_no() > 1:
            self.set_font('Liberation', 'I', 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 5, 'Options Menu Demo \u2014 Lab 3 Homework 3', new_x="LMARGIN", new_y="TOP", align='L')
            self.cell(0, 5, f'Page {self.page_no()}', new_x="LMARGIN", new_y="NEXT", align='R')
            self.line(10, 12, 200, 12)
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('Liberation', 'I', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Patrick Kilonzo Mbithi  |  SCT211-0036/2025  |  BSc Computer Science  |  Dr. Lawrence Nderu', new_x="LMARGIN", new_y="NEXT", align='C')

    def section_title(self, number, title):
        self.set_font('Liberation', 'B', 16)
        self.set_text_color(0, 51, 93)
        self.cell(0, 10, f'{number} \u00b7 {title}', new_x="LMARGIN", new_y="NEXT", align='L')
        self.set_draw_color(0, 51, 93)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def subsection_title(self, number, title):
        self.set_font('Liberation', 'B', 13)
        self.set_text_color(0, 70, 120)
        self.cell(0, 8, f'{number} {title}', new_x="LMARGIN", new_y="NEXT", align='L')
        self.ln(2)

    def body_text(self, text):
        self.set_font('Liberation', '', 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def bold_text(self, text):
        self.set_font('Liberation', 'B', 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5, text)
        self.ln(1)

    def code_block(self, code_lines, font_size=8):
        self.set_font('LiberationMono', '', font_size)
        self.set_text_color(40, 40, 40)
        self.set_fill_color(240, 240, 245)
        y = self.get_y()
        line_h = font_size * 0.5 + 1
        block_h = len(code_lines) * line_h + 6
        if y + block_h > 275:
            self.add_page()
            y = self.get_y()
        self.rect(10, y, 190, block_h, 'F')
        self.set_xy(12, y + 3)
        for line in code_lines:
            self.cell(0, line_h, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def table_row(self, cells, widths, header=False):
        self.set_font('Liberation', 'B' if header else '', 9)
        if header:
            self.set_text_color(255, 255, 255)
            self.set_fill_color(0, 51, 93)
        else:
            self.set_text_color(30, 30, 30)
            self.set_fill_color(245, 245, 250)
        h = 7
        x_start = self.get_x()
        y_start = self.get_y()
        if y_start + h > 275:
            self.add_page()
            y_start = self.get_y()
        for i, (cell, w) in enumerate(zip(cells, widths)):
            self.set_xy(x_start + sum(widths[:i]), y_start)
            self.cell(w, h, cell, 1, 0, 'L', True)
        self.ln(h)

    def checklist_item(self, text, checked=False):
        self.set_font('Liberation', '', 10)
        self.set_text_color(30, 30, 30)
        checkbox = '[X]' if checked else '[ ]'
        self.cell(0, 6, f'  {checkbox}  {text}', new_x="LMARGIN", new_y="NEXT")


def generate_pdf():
    pdf = LabReportPDF()
    
    # ==================== PAGE 1: TITLE PAGE ====================
    pdf.add_page()
    pdf.ln(30)
    
    # Course header
    pdf.set_font('Liberation', 'B', 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, 'JKUAT  |  ICS 2300  |  MOBILE APPLICATION DEVELOPMENT', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(10)
    
    # Main title
    pdf.set_font('Liberation', 'B', 30)
    pdf.set_text_color(0, 51, 93)
    pdf.cell(0, 14, 'Options Menu Demo', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(4)
    
    # Subtitle
    pdf.set_font('Liberation', '', 16)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 10, 'Options Menu, Navigation and Toast Feedback', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(6)
    
    # Description
    pdf.set_font('Liberation', '', 12)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 7, 'An Android (Java) walkthrough: implementing an options menu with\nthree actions, handling selections with Toast feedback,\nnavigating between activities, and diagnosing a deliberate fault.', align='C')
    pdf.ln(20)
    
    # Meta info
    pdf.set_font('Liberation', '', 11)
    pdf.set_text_color(40, 40, 40)
    meta_items = [
        ('Student', 'Patrick Kilonzo Mbithi'),
        ('Reg. Number', 'SCT211-0036/2025'),
        ('Course', 'BSc Computer Science'),
        ('Instructor', 'Dr. Lawrence Nderu'),
        ('Lab', 'Lab 3 Homework 3 (Consolidated)'),
        ('Date', 'November 2026'),
        ('Environment', 'Android Studio Koala | API 34 | Java 11'),
    ]
    for label, value in meta_items:
        pdf.set_font('Liberation', 'B', 11)
        pdf.cell(45, 8, label + ':', new_x="RIGHT", new_y="TOP")
        pdf.set_font('Liberation', '', 11)
        pdf.cell(0, 8, value, new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(20)
    
    # Academic integrity
    pdf.set_font('Liberation', 'I', 9)
    pdf.set_text_color(120, 120, 120)
    pdf.multi_cell(0, 5, 'This report documents the actual implementation. All code and screenshots\nreflect the working application. AI assistance was used for PDF generation only;\nall application code was written and verified by the student.', align='C')
    
    
    # ==================== PAGE 2: LAB OBJECTIVE ====================
    pdf.add_page()
    pdf.section_title('1', 'Lab Objective')
    
    pdf.body_text(
        'The goal of this lab is to build an interactive Android application that demonstrates '
        'the complete lifecycle of an Options Menu: declaring the menu in XML, attaching it to '
        'the Activity via onCreateOptionsMenu(), handling user selections in '
        'onOptionsItemSelected(), providing appropriate user feedback via Toast and AlertDialog, '
        'and navigating to a second screen (Activity) with correct Back button behavior.'
    )
    
    pdf.body_text('By the end of this lab the app can:')
    
    pdf.set_font('Liberation', '', 10)
    pdf.set_text_color(30, 30, 30)
    features = [
        'Display an Options Menu with three meaningful actions: Add Record, View Records, About',
        'Show Toast messages for brief, non-critical feedback on each menu action',
        'Navigate to a second Activity (RecordsActivity) when "View Records" is selected',
        'Return via Back button without duplicating actions or losing state',
        'Demonstrate a deliberate fault (incorrect item ID) with symptom, cause, and correction',
        'Persist menu state across configuration changes (rotation) using onSaveInstanceState',
    ]
    for i, feat in enumerate(features, 1):
        pdf.cell(8, 6, '')
        pdf.cell(0, 6, f'{i}.  {feat}', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    
    # Component table
    pdf.subsection_title('1.1', 'Key Components Used')
    
    col_widths = [55, 135]
    pdf.table_row(['Component', 'Purpose in this app'], col_widths, header=True)
    pdf.table_row(['Menu XML (res/menu/options_menu.xml)', 'Declares three items with stable IDs, titles, icons, and showAsAction'], col_widths)
    pdf.table_row(['onCreateOptionsMenu()', 'Inflates the menu resource and attaches it to the action bar'], col_widths)
    pdf.table_row(['onOptionsItemSelected()', 'Routes each item ID to its handler; demonstrates deliberate fault'], col_widths)
    pdf.table_row(['Toast', 'Brief non-critical feedback (Add Record, View Records, About)'], col_widths)
    pdf.table_row(['AlertDialog.Builder', 'Modal confirmation for About; fault explanation dialog'], col_widths)
    pdf.table_row(['Intent + startActivity()', 'Launches RecordsActivity for "View Records"'], col_widths)
    pdf.table_row(['RecordManager (singleton)', 'In-memory storage for records shared between activities'], col_widths)
    pdf.table_row(['onSaveInstanceState()', 'Preserves fault-demo flag across rotation/recreation'], col_widths)
    
    
    # ==================== PAGE 3: HOW THE APP WORKS ====================
    pdf.add_page()
    pdf.section_title('2', 'How the App Works')
    
    pdf.body_text(
        'Before writing code, it helps to see the user journey. The app has a single main screen '
        'with an action bar menu, and a second screen for viewing records. The decision points '
        'are: which menu item was selected, and whether the fault demo is active.'
    )
    
    pdf.subsection_title('2.1', 'User Journey')
    
    journey_steps = [
        ('Launch App', 'MainActivity starts, shows instructional UI'),
        ('Open Menu', 'User taps ... (three-dot) in action bar'),
        ('Select "Add Record"', 'Toast appears, record added to singleton'),
        ('Select "View Records"', 'Toast appears, RecordsActivity launched'),
        ('Press Back', 'Returns to MainActivity, no duplicate action'),
        ('Select "About"', 'Toast + AlertDialog with app info'),
        ('Toggle Fault Demo', 'Button or menu item enables incorrect ID mode'),
        ('Select "Add Record" (fault ON)', 'Wrong handler runs: shows "View Records" toast'),
        ('Toggle Fault OFF', 'Normal operation restored'),
    ]
    
    pdf.set_font('Liberation', '', 9)
    col_w = [30, 160]
    pdf.table_row(['Step', 'Description'], col_w, header=True)
    for step, desc in journey_steps:
        pdf.table_row([step, desc], col_w)
    
    pdf.ln(4)
    
    pdf.subsection_title('2.2', 'Event Flow for "View Records" (Screen Change)')
    
    pdf.body_text(
        'When the user selects "View Records" from the options menu:\n\n'
        '1. onOptionsItemSelected(MenuItem) receives the click event\n'
        '2. Switch statement matches R.id.menu_view_records\n'
        '3. handleViewRecords() is called\n'
        '4. Toast feedback shown: "Opening records list..."\n'
        '5. Intent created: new Intent(this, RecordsActivity.class)\n'
        '6. startActivity(intent) launches the new Activity\n'
        '7. RecordsActivity.onCreate() inflates its layout, loads records from RecordManager\n'
        '8. User views list; pressing BACK calls finish() on RecordsActivity\n'
        '9. MainActivity.onResume() fires \u2014 but NO duplicate action occurs because:\n'
        '   - MainActivity was not destroyed (only paused)\n'
        '   - onCreate() is NOT called again\n'
        '   - No onNewIntent() override exists to re-trigger the action\n'
        '10. Fault-demo flag is preserved via onSaveInstanceState()/restore'
    )
    
    
    # ==================== PAGE 4: PROJECT STRUCTURE ====================
    pdf.add_page()
    pdf.section_title('3', 'Project Structure')
    
    pdf.body_text('The project follows standard Android conventions with a few key additions:')
    
    pdf.set_font('LiberationMono', '', 9)
    pdf.set_text_color(40, 40, 40)
    structure_lines = [
        'Options_menu/',
        '  app/',
        '    src/main/',
        '      java/com/example/options_menu/',
        '        MainActivity.java        <-- Logic: menu, toasts, navigation, fault demo',
        '        RecordsActivity.java     <-- Second screen: ListView of records',
        '        RecordManager.java       <-- Singleton in-memory record storage',
        '      res/',
        '        layout/',
        '          activity_main.xml      <-- Main UI with instructions + fault toggle',
        '          activity_records.xml   <-- ListView + empty state',
        '        menu/',
        '          options_menu.xml       <-- 4 menu items with stable IDs',
        '        values/',
        '          strings.xml            <-- All user-facing text',
        '          themes.xml             <-- Material3 DayNight theme',
        '        AndroidManifest.xml      <-- Declares both activities, parent link',
    ]
    pdf.code_block(structure_lines, font_size=8)
    
    pdf.ln(2)
    pdf.bold_text('\u26A0 Watch out.')
    pdf.body_text(
        'The theme MUST inherit from Theme.Material3.DayNight (or MaterialComponents) '
        'to support modern UI components. A plain AppCompat theme would work for this '
        'simple app but Material3 is the current standard and provides better defaults.'
    )
    
    
    # ==================== PAGE 5: MENU RESOURCE ====================
    pdf.add_page()
    pdf.section_title('4', 'Menu Resource (res/menu/options_menu.xml)')
    
    pdf.subsection_title('4.1', 'Complete Menu XML')
    
    pdf.body_text(
        'The menu is declared in XML. Each item has a stable ID (R.id.menu_*), a title '
        'from strings.xml, an optional system icon, and a showAsAction attribute '
        'controlling action bar visibility.'
    )
    
    menu_xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<menu xmlns:android="http://schemas.android.com/apk/res/android"',
        '    xmlns:app="http://schemas.android.com/apk/res-auto">',
        '',
        '    <item',
        '        android:id="@+id/menu_add_record"',
        '        android:title="@string/menu_add_record"',
        '        android:icon="@android:drawable/ic_menu_add"',
        '        app:showAsAction="ifRoom|withText" />',
        '',
        '    <item',
        '        android:id="@+id/menu_view_records"',
        '        android:title="@string/menu_view_records"',
        '        android:icon="@android:drawable/ic_menu_view"',
        '        app:showAsAction="ifRoom|withText" />',
        '',
        '    <item',
        '        android:id="@+id/menu_about"',
        '        android:title="@string/menu_about"',
        '        android:icon="@android:drawable/ic_menu_info_details"',
        '        app:showAsAction="never" />',
        '',
        '    <item',
        '        android:id="@+id/menu_toggle_fault"',
        '        android:title="@string/menu_toggle_fault"',
        '        android:icon="@android:drawable/ic_menu_manage"',
        '        app:showAsAction="never" />',
        '',
        '</menu>',
    ]
    pdf.code_block(menu_xml, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('4.2', 'Key Points')
    
    pdf.body_text(
        '\u2022 Stable IDs: Using @+id/menu_add_record generates R.id.menu_add_record at compile time.\n'
        '\u2022 String resources: Titles come from strings.xml for localization support.\n'
        '\u2022 showAsAction: "ifRoom|withText" shows icon+text if space permits; "never" forces overflow.\n'
        '\u2022 System icons: @android:drawable/ic_menu_* provides consistent platform icons.\n'
        '\u2022 Attachment: The menu is attached to the Activity by inflating it in onCreateOptionsMenu().'
    )
    
    
    # ==================== PAGE 6: MAIN ACTIVITY LAYOUT ====================
    pdf.add_page()
    pdf.section_title('5', 'Main Activity Layout (res/layout/activity_main.xml)')
    
    pdf.subsection_title('5.1', 'Complete Layout XML')
    
    pdf.body_text(
        'The main screen uses ConstraintLayout for flexible positioning. It displays the app title, '
        'instructional text explaining the three menu actions, a button to toggle the fault demo, '
        'and a status indicator showing whether the fault mode is active.'
    )
    
    layout_xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<androidx.constraintlayout.widget.ConstraintLayout',
        '    xmlns:android="http://schemas.android.com/apk/res/android"',
        '    xmlns:app="http://schemas.android.com/apk/res-auto"',
        '    xmlns:tools="http://schemas.android.com/tools"',
        '    android:id="@+id/main"',
        '    android:layout_width="match_parent"',
        '    android:layout_height="match_parent"',
        '    android:padding="16dp"',
        '    tools:context=".MainActivity">',
        '',
        '    <!-- Title -->',
        '    <TextView',
        '        android:id="@+id/textViewTitle"',
        '        android:layout_width="wrap_content"',
        '        android:layout_height="wrap_content"',
        '        android:text="@string/app_name"',
        '        android:textSize="28sp"',
        '        android:textStyle="bold"',
        '        app:layout_constraintEnd_toEndOf="parent"',
        '        app:layout_constraintStart_toStartOf="parent"',
        '        app:layout_constraintTop_toTopOf="parent"',
        '        android:layout_marginTop="32dp" />',
        '',
        '    <!-- Subtitle -->',
        '    <TextView',
        '        android:id="@+id/textViewSubtitle"',
        '        android:layout_width="wrap_content"',
        '        android:layout_height="wrap_content"',
        '        android:text="Options Menu Demo\\nICS 2300 - Lab 3 Homework 3"',
        '        android:textSize="16sp"',
        '        android:textColor="@android:color/darker_gray"',
        '        android:gravity="center"',
        '        app:layout_constraintEnd_toEndOf="parent"',
        '        app:layout_constraintStart_toStartOf="parent"',
        '        app:layout_constraintTop_toBottomOf="@id/textViewTitle"',
        '        android:layout_marginTop="8dp" />',
        '',
        '    <!-- Divider -->',
        '    <View',
        '        android:id="@+id/divider"',
        '        android:layout_width="match_parent"',
        '        android:layout_height="1dp"',
        '        android:background="@android:color/darker_gray"',
        '        app:layout_constraintTop_toBottomOf="@id/textViewSubtitle"',
        '        android:layout_marginTop="24dp"',
        '        android:layout_marginBottom="24dp" />',
        '',
        '    <!-- Instruction Text (from strings.xml) -->',
        '    <TextView',
        '        android:id="@+id/textViewInstructions"',
        '        android:layout_width="0dp"',
        '        android:layout_height="wrap_content"',
        '        android:text="@string/instructions_main"',
        '        android:textSize="14sp"',
        '        app:layout_constraintEnd_toEndOf="parent"',
        '        app:layout_constraintStart_toStartOf="parent"',
        '        app:layout_constraintTop_toBottomOf="@id/divider"',
        '        android:layout_marginHorizontal="16dp" />',
        '',
        '    <!-- Fault Demo Toggle Button -->',
        '    <Button',
        '        android:id="@+id/buttonToggleFault"',
        '        android:layout_width="wrap_content"',
        '        android:layout_height="wrap_content"',
        '        android:text="@string/toggle_fault_demo"',
        '        android:onClick="onToggleFaultClick"',
        '        app:layout_constraintEnd_toEndOf="parent"',
        '        app:layout_constraintStart_toStartOf="parent"',
        '        app:layout_constraintTop_toBottomOf="@id/textViewInstructions"',
        '        android:layout_marginTop="32dp" />',
        '',
        '    <!-- Status Indicator -->',
        '    <TextView',
        '        android:id="@+id/textViewFaultStatus"',
        '        android:layout_width="wrap_content"',
        '        android:layout_height="wrap_content"',
        '        android:text="@string/fault_status_off"',
        '        android:textSize="14sp"',
        '        android:textColor="@android:color/holo_green_dark"',
        '        app:layout_constraintEnd_toEndOf="parent"',
        '        app:layout_constraintStart_toStartOf="parent"',
        '        app:layout_constraintTop_toBottomOf="@id/buttonToggleFault"',
        '        android:layout_marginTop="16dp" />',
        '',
        '    <!-- Menu Reference -->',
        '    <TextView',
        '        android:id="@+id/textViewMenuRef"',
        '        android:layout_width="0dp"',
        '        android:layout_height="wrap_content"',
        '        android:text="@string/menu_reference"',
        '        android:textSize="13sp"',
        '        android:textColor="@android:color/darker_gray"',
        '        app:layout_constraintEnd_toEndOf="parent"',
        '        app:layout_constraintStart_toStartOf="parent"',
        '        app:layout_constraintTop_toBottomOf="@id/textViewFaultStatus"',
        '        android:layout_marginTop="32dp"',
        '        android:layout_marginHorizontal="16dp" />',
        '',
        '</androidx.constraintlayout.widget.ConstraintLayout>',
    ]
    pdf.code_block(layout_xml, font_size=7.5)
    
    
    # ==================== PAGE 7: RECORDS ACTIVITY LAYOUT ====================
    pdf.add_page()
    pdf.section_title('6', 'Records Activity Layout (res/layout/activity_records.xml)')
    
    pdf.subsection_title('6.1', 'Complete Layout XML')
    
    pdf.body_text(
        'The second screen displays stored records in a ListView. An empty-state TextView '
        'is shown when no records exist. Both views share the same constraints; visibility '
        'is toggled programmatically in RecordsActivity.'
    )
    
    records_xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<androidx.constraintlayout.widget.ConstraintLayout',
        '    xmlns:android="http://schemas.android.com/apk/res/android"',
        '    xmlns:app="http://schemas.android.com/apk/res-auto"',
        '    xmlns:tools="http://schemas.android.com/tools"',
        '    android:id="@+id/records_main"',
        '    android:layout_width="match_parent"',
        '    android:layout_height="match_parent"',
        '    tools:context=".RecordsActivity">',
        '',
        '    <!-- Empty State (initially hidden) -->',
        '    <TextView',
        '        android:id="@+id/textViewEmpty"',
        '        android:layout_width="wrap_content"',
        '        android:layout_height="wrap_content"',
        '        android:text="@string/empty_records_list"',
        '        android:textSize="16sp"',
        '        android:textColor="@android:color/darker_gray"',
        '        android:gravity="center"',
        '        android:layout_margin="24dp"',
        '        android:visibility="gone"',
        '        app:layout_constraintBottom_toBottomOf="parent"',
        '        app:layout_constraintEnd_toEndOf="parent"',
        '        app:layout_constraintStart_toStartOf="parent"',
        '        app:layout_constraintTop_toTopOf="parent" />',
        '',
        '    <!-- Records List -->',
        '    <ListView',
        '        android:id="@+id/listViewRecords"',
        '        android:layout_width="0dp"',
        '        android:layout_height="0dp"',
        '        android:layout_margin="16dp"',
        '        android:divider="@android:color/darker_gray"',
        '        android:dividerHeight="1dp"',
        '        android:visibility="visible"',
        '        app:layout_constraintBottom_toBottomOf="parent"',
        '        app:layout_constraintEnd_toEndOf="parent"',
        '        app:layout_constraintStart_toStartOf="parent"',
        '        app:layout_constraintTop_toTopOf="parent" />',
        '',
        '</androidx.constraintlayout.widget.ConstraintLayout>',
    ]
    pdf.code_block(records_xml, font_size=8)
    
    
    # ==================== PAGE 8: MAIN ACTIVITY - IMPORTS & FIELDS ====================
    pdf.add_page()
    pdf.section_title('7', 'MainActivity.java \u2014 Imports & Fields')
    
    pdf.subsection_title('7.1', 'Imports')
    
    pdf.body_text(
        'All necessary Android framework classes are imported. Note the use of '
        'androidx.appcompat.app.AlertDialog and the Material3 theme compatibility.'
    )
    
    imports = [
        'package com.example.options_menu;',
        '',
        'import android.content.Intent;',
        'import android.os.Bundle;',
        'import android.util.Log;',
        'import android.view.Menu;',
        'import android.view.MenuItem;',
        'import android.view.View;',
        'import android.widget.TextView;',
        'import android.widget.Toast;',
        '',
        'import androidx.activity.EdgeToEdge;',
        'import androidx.appcompat.app.AlertDialog;',
        'import androidx.appcompat.app.AppCompatActivity;',
        'import androidx.core.graphics.Insets;',
        'import androidx.core.view.ViewCompat;',
        'import androidx.core.view.WindowInsetsCompat;',
    ]
    pdf.code_block(imports, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('7.2', 'Class Definition & Fields')
    
    pdf.body_text(
        'A single boolean field tracks the fault demonstration state. It is persisted '
        'across configuration changes via onSaveInstanceState().'
    )
    
    fields = [
        'public class MainActivity extends AppCompatActivity {',
        '',
        '    private static final String TAG = "MainActivity";',
        '',
        '    // Flag to demonstrate fault: when true, uses WRONG item ID in switch case',
        '    private boolean demonstrateFault = false;',
        '',
        '    @Override',
        '    protected void onCreate(Bundle savedInstanceState) {',
        '        // ...',
        '    }',
    ]
    pdf.code_block(fields, font_size=8)
    
    
    # ==================== PAGE 9: MAIN ACTIVITY - ONCREATE ====================
    pdf.add_page()
    pdf.section_title('8', 'MainActivity.java \u2014 onCreate & Menu Inflation')
    
    pdf.subsection_title('8.1', 'onCreate() \u2014 View Binding & State Restoration')
    
    pdf.body_text(
        'onCreate() sets up EdgeToEdge display, inflates the layout, applies window insets '
        'for system bars, and restores the fault-demo flag if the Activity was recreated '
        '(e.g., due to rotation).'
    )
    
    oncreate = [
        '@Override',
        'protected void onCreate(Bundle savedInstanceState) {',
        '    super.onCreate(savedInstanceState);',
        '    Log.d(TAG, "onCreate called");',
        '    EdgeToEdge.enable(this);',
        '    setContentView(R.layout.activity_main);',
        '',
        '    ViewCompat.setOnApplyWindowInsetsListener(',
        '        findViewById(R.id.main), (v, insets) -> {',
        '            Insets systemBars = insets.getInsets(',
        '                WindowInsetsCompat.Type.systemBars());',
        '            v.setPadding(systemBars.left, systemBars.top,',
        '                systemBars.right, systemBars.bottom);',
        '            return insets;',
        '        });',
        '',
        '    // Restore fault demonstration state if activity recreated',
        '    if (savedInstanceState != null) {',
        '        demonstrateFault = savedInstanceState.',
        '            getBoolean("demonstrateFault", false);',
        '        Log.d(TAG, "Restored demonstrateFault: " + demonstrateFault);',
        '    }',
        '}',
    ]
    pdf.code_block(oncreate, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('8.2', 'onSaveInstanceState() \u2014 Persisting the Flag')
    
    pdf.body_text(
        'The fault-demo flag must survive rotation and process recreation. This is done by '
        'saving it in the Bundle and restoring it in onCreate().'
    )
    
    savestate = [
        '@Override',
        'protected void onSaveInstanceState(Bundle outState) {',
        '    super.onSaveInstanceState(outState);',
        '    outState.putBoolean("demonstrateFault", demonstrateFault);',
        '    Log.d(TAG, "Saved demonstrateFault: " + demonstrateFault);',
        '}',
    ]
    pdf.code_block(savestate, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('8.3', 'onCreateOptionsMenu() \u2014 Attaching the Menu')
    
    pdf.body_text(
        'This is where the menu resource is inflated and attached to the Activity\'s action bar. '
        'Returning true tells the system the menu should be shown.'
    )
    
    menu_inflate = [
        '@Override',
        'public boolean onCreateOptionsMenu(Menu menu) {',
        '    Log.d(TAG, "onCreateOptionsMenu called");',
        '    getMenuInflater().inflate(R.menu.options_menu, menu);',
        '    return true;',
        '}',
    ]
    pdf.code_block(menu_inflate, font_size=8)
    
    
    # ==================== PAGE 10: MAIN ACTIVITY - OPTIONS ITEM SELECTED ====================
    pdf.add_page()
    pdf.section_title('9', 'MainActivity.java \u2014 onOptionsItemSelected()')
    
    pdf.subsection_title('9.1', 'Complete Handler with Fault Demo')
    
    pdf.body_text(
        'This method is the central routing point for all menu selections. It uses a '
        'switch-like if/else chain on the stable item ID. When the fault demo is active, '
        'it deliberately substitutes the WRONG item ID to demonstrate the symptom of '
        'incorrect ID handling.'
    )
    
    handler = [
        '@Override',
        'public boolean onOptionsItemSelected(MenuItem item) {',
        '    int itemId = item.getItemId();',
        '    Log.d(TAG, "onOptionsItemSelected: itemId=" + itemId',
        '        + ", demonstrateFault=" + demonstrateFault);',
        '',
        '    // DEMONSTRATE FAULT: Use incorrect ID when flag is set',
        '    // This simulates a common bug where developer uses wrong constant',
        '    int effectiveItemId = demonstrateFault',
        '        ? R.id.menu_view_records  // WRONG ID',
        '        : itemId;                  // CORRECT ID',
        '',
        '    if (effectiveItemId != itemId) {',
        '        Log.w(TAG, "FAULT DEMONSTRATION: Using wrong ID '
        '+ effectiveItemId + " instead of " + itemId);',
        '    }',
        '',
        '    if (effectiveItemId == R.id.menu_add_record) {',
        '        handleAddRecord();',
        '        return true;',
        '    } else if (effectiveItemId == R.id.menu_view_records) {',
        '        handleViewRecords();',
        '        return true;',
        '    } else if (effectiveItemId == R.id.menu_about) {',
        '        handleAbout();',
        '        return true;',
        '    } else if (itemId == R.id.menu_toggle_fault) {',
        '        // Control item uses actual itemId, not effectiveItemId',
        '        onToggleFaultClick(null);',
        '        return true;',
        '    }',
        '',
        '    // Safe fallback for unhandled items',
        '    Log.w(TAG, "Unhandled menu item ID: " + itemId);',
        '    Toast.makeText(this, "Unknown action", Toast.LENGTH_SHORT).show();',
        '    return super.onOptionsItemSelected(item);',
        '}',
    ]
    pdf.code_block(handler, font_size=7.5)
    
    pdf.ln(2)
    pdf.subsection_title('9.2', 'Why Use Item ID Instead of Displayed Label?')
    
    pdf.body_text(
        'Stable IDs (R.id.menu_add_record) are compile-time constants that never change. '
        'Display labels are user-facing strings that can change due to:\n'
        '\u2022 Localization (different languages)\n'
        '\u2022 UI redesigns (changing "Add Record" to "New Entry")\n'
        '\u2022 A/B testing variants\n'
        '\u2022 Accessibility adjustments\n\n'
        'If code compared against the label text, any of these changes would silently break '
        'the handler. IDs provide a stable contract between XML declaration and Java logic.'
    )
    
    
    # ==================== PAGE 11: MAIN ACTIVITY - ACTION HANDLERS ====================
    pdf.add_page()
    pdf.section_title('10', 'MainActivity.java \u2014 Action Handlers')
    
    pdf.subsection_title('10.1', 'handleAddRecord() \u2014 Toast Feedback + Data Update')
    
    pdf.body_text(
        'Shows a brief Toast, adds a timestamped record to the singleton manager, '
        'then shows a confirmation Toast. Toasts are appropriate here because the '
        'action succeeds immediately and requires no user acknowledgment.'
    )
    
    add_record = [
        'private void handleAddRecord() {',
        '    Log.d(TAG, "handleAddRecord called");',
        '',
        '    // Brief non-critical feedback via Toast',
        '    Toast.makeText(this, R.string.toast_add_record,',
        '        Toast.LENGTH_SHORT).show();',
        '',
        '    // Add a new record to the shared manager',
        '    String newRecord = "Record #"',
        '        + (RecordManager.getInstance().getCount() + 1)',
        '        + " - Added at "',
        '        + java.time.LocalTime.now().toString().substring(0, 8);',
        '    RecordManager.getInstance().addRecord(newRecord);',
        '',
        '    // Follow-up confirmation Toast',
        '    Toast.makeText(this, R.string.toast_record_added,',
        '        Toast.LENGTH_SHORT).show();',
        '',
        '    Log.d(TAG, "Record added: " + newRecord);',
        '}',
    ]
    pdf.code_block(add_record, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('10.2', 'handleViewRecords() \u2014 Screen Navigation')
    
    pdf.body_text(
        'Launches RecordsActivity via explicit Intent. The event path and Back behavior '
        'are documented in the method comments.'
    )
    
    view_records = [
        'private void handleViewRecords() {',
        '    Log.d(TAG, "handleViewRecords called - starting RecordsActivity");',
        '',
        '    Toast.makeText(this, R.string.toast_view_records,',
        '        Toast.LENGTH_SHORT).show();',
        '',
        '    Intent intent = new Intent(this, RecordsActivity.class);',
        '    startActivity(intent);',
        '}',
    ]
    pdf.code_block(view_records, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('10.3', 'handleAbout() \u2014 Modal Dialog (Not Toast)')
    
    pdf.body_text(
        'Shows an AlertDialog with app information. This is a case where Toast is '
        'UNSUITABLE \u2014 the content is multi-line, must remain visible until dismissed, '
        'and provides meaningful information the user may want to read fully.'
    )
    
    about = [
        'private void handleAbout() {',
        '    Log.d(TAG, "handleAbout called");',
        '',
        '    Toast.makeText(this, R.string.toast_about,',
        '    Toast.LENGTH_SHORT).show();',
        '',
        '    new AlertDialog.Builder(this)',
        '        .setTitle(R.string.about_title)',
        '        .setMessage(R.string.about_message)',
        '        .setPositiveButton(R.string.about_ok, null)',
        '        .show();',
        '}',
    ]
    pdf.code_block(about, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('10.4', 'When is Toast UNSUITABLE Feedback?')
    
    pdf.body_text(
        'Toast should NOT be used when:\n'
        '\u2022 The message is long or multi-line (toasts are single-line by design)\n'
        '\u2022 The information requires user acknowledgment or action\n'
        '\u2022 The content includes critical warnings or errors that must not be missed\n'
        '\u2022 The user needs to copy or interact with the text\n'
        '\u2022 The app state changes significantly and the user must be explicitly informed\n\n'
        'In those cases, use AlertDialog, Snackbar (with action), or a dedicated UI state.'
    )
    
    
    # ==================== PAGE 12: MAIN ACTIVITY - FAULT DEMO ====================
    pdf.add_page()
    pdf.section_title('11', 'MainActivity.java \u2014 Fault Demonstration')
    
    pdf.subsection_title('11.1', 'Toggle Fault Handler')
    
    pdf.body_text(
        'Called from both the UI button and the menu item. Updates the flag, refreshes '
        'the status TextView, shows Toast feedback, and when enabling, displays the '
        'explanatory AlertDialog.'
    )
    
    toggle_fault = [
        'public void onToggleFaultClick(View view) {',
        '    demonstrateFault = !demonstrateFault;',
        '    Log.d(TAG, "Fault demo toggled via button: " + demonstrateFault);',
        '',
        '    // Update status text',
        '    TextView statusText = findViewById(R.id.textViewFaultStatus);',
        '    if (demonstrateFault) {',
        '        statusText.setText(R.string.fault_status_on);',
        '        statusText.setTextColor(getColor(android.R.color.holo_red_dark));',
        '    } else {',
        '        statusText.setText(R.string.fault_status_off);',
        '        statusText.setTextColor(getColor(android.R.color.holo_green_dark));',
        '    }',
        '',
        '    // Show Toast feedback',
        '    String status = demonstrateFault',
        '        ? "ENABLED (incorrect ID will be used)"',
        '        : "DISABLED (correct ID used)";',
        '    Toast.makeText(this, "Fault Demo: " + status,',
        '        Toast.LENGTH_LONG).show();',
        '',
        '    if (demonstrateFault) {',
        '        showFaultExplanation();',
        '    }',
        '}',
    ]
    pdf.code_block(toggle_fault, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('11.2', 'Fault Explanation Dialog')
    
    pdf.body_text(
        'When the fault is enabled, this dialog appears to explain what was deliberately '
        'broken. This turns the fault into a teaching moment.'
    )
    
    fault_expl = [
        'private void showFaultExplanation() {',
        '    new AlertDialog.Builder(this)',
        '        .setTitle(R.string.fault_explanation_title)',
        '        .setMessage(R.string.fault_explanation_message)',
        '        .setPositiveButton(R.string.ok, null)',
        '        .show();',
        '}',
    ]
    pdf.code_block(fault_expl, font_size=8)
    
    pdf.ln(2)
    pdf.subsection_title('11.3', 'Fault Record: Incorrect Item ID')
    
    pdf.body_text(
        'Deliberate Fault: In onOptionsItemSelected(), when demonstrateFault=true, '
        'the code substitutes R.id.menu_view_records for the actual item ID.\n\n'
        'Observed Symptom: User selects "Add Record" -> Toast says "Opening records list..." '
        '(the View Records message) instead of "Add Record action selected".\n\n'
        'Root Cause: The switch/if-chain matches on the WRONG constant. The handler for '
        'View Records is executed instead of the handler for Add Record.\n\n'
        'Correction: Toggle the fault OFF (button or menu). The code then uses the actual '
        'itemId: effectiveItemId = itemId. Selection now routes to the correct handler.\n\n'
        'Retest: After toggling OFF, selecting "Add Record" shows the correct Toast and '
        'adds a record. Selecting "View Records" correctly opens the records screen.\n\n'
        'Lesson: This confirms why stable IDs matter and why copy-paste errors in '
        'switch cases are dangerous \u2014 the compiler cannot detect them.'
    )
    
    
    # ==================== PAGE 13: RECORDSACTIVITY ====================
    pdf.add_page()
    pdf.section_title('12', 'RecordsActivity.java \u2014 Complete Source')
    
    pdf.body_text(
        'Displays the list of records from the shared RecordManager. Refreshes in onResume() '
        'to reflect any additions made in MainActivity. Uses a simple ArrayAdapter with the '
        'platform\'s simple_list_item_1 layout.'
    )
    
    records_act = [
        'package com.example.options_menu;',
        '',
        'import android.content.Intent;',
        'import android.os.Bundle;',
        'import android.util.Log;',
        'import android.view.View;',
        'import android.widget.AdapterView;',
        'import android.widget.ArrayAdapter;',
        'import android.widget.ListView;',
        'import android.widget.TextView;',
        'import android.widget.Toast;',
        '',
        'import androidx.activity.EdgeToEdge;',
        'import androidx.appcompat.app.AppCompatActivity;',
        'import androidx.core.graphics.Insets;',
        'import androidx.core.view.ViewCompat;',
        'import androidx.core.view.WindowInsetsCompat;',
        '',
        'import java.util.ArrayList;',
        'import java.util.List;',
        '',
        '/**',
        ' * RecordsActivity displays the list of stored records.',
        ' * Demonstrates screen change and proper Back navigation.',
        ' */',
        'public class RecordsActivity extends AppCompatActivity {',
        '',
        '    private static final String TAG = "RecordsActivity";',
        '',
        '    private ListView listViewRecords;',
        '    private TextView textViewEmpty;',
        '    private ArrayAdapter<String> recordsAdapter;',
        '    private List<String> recordsList;',
        '',
        '    @Override',
        '    protected void onCreate(Bundle savedInstanceState) {',
        '        super.onCreate(savedInstanceState);',
        '        Log.d(TAG, "onCreate called");',
        '        EdgeToEdge.enable(this);',
        '        setContentView(R.layout.activity_records);',
        '',
        '        ViewCompat.setOnApplyWindowInsetsListener(',
        '            findViewById(R.id.records_main), (v, insets) -> {',
        '                Insets systemBars = insets.getInsets(',
        '                    WindowInsetsCompat.Type.systemBars());',
        '                v.setPadding(systemBars.left, systemBars.top,',
        '                    systemBars.right, systemBars.bottom);',
        '                return insets;',
        '            });',
        '',
        '        listViewRecords = findViewById(R.id.listViewRecords);',
        '        textViewEmpty = findViewById(R.id.textViewEmpty);',
        '',
        '        recordsList = RecordManager.getInstance().getRecords();',
        '        recordsAdapter = new ArrayAdapter<>(this,',
        '            android.R.layout.simple_list_item_1, recordsList);',
        '        listViewRecords.setAdapter(recordsAdapter);',
        '',
        '        updateEmptyState();',
        '',
        '        listViewRecords.setOnItemClickListener(',
        '            (parent, view, position, id) -> {',
        '                String record = recordsList.get(position);',
        '                Toast.makeText(this,',
        '                    "Selected: " + record, Toast.LENGTH_SHORT).show();',
        '            });',
        '    }',
        '',
        '    @Override',
        '    protected void onResume() {',
        '        super.onResume();',
        '        Log.d(TAG, "onResume called");',
        '        refreshRecords();',
        '    }',
        '',
        '    private void refreshRecords() {',
        '        recordsList.clear();',
        '        recordsList.addAll(RecordManager.getInstance().getRecords());',
        '        recordsAdapter.notifyDataSetChanged();',
        '        updateEmptyState();',
        '    }',
        '',
        '    private void updateEmptyState() {',
        '        if (recordsList.isEmpty()) {',
        '            listViewRecords.setVisibility(View.GONE);',
        '            textViewEmpty.setVisibility(View.VISIBLE);',
        '        } else {',
        '            listViewRecords.setVisibility(View.VISIBLE);',
        '            textViewEmpty.setVisibility(View.GONE);',
        '        }',
        '    }',
        '}',
    ]
    pdf.code_block(records_act, font_size=7)
    
    
    # ==================== PAGE 14: RECORD MANAGER ====================
    pdf.add_page()
    pdf.section_title('13', 'RecordManager.java \u2014 Shared Data Store')
    
    pdf.body_text(
        'A thread-safe singleton providing in-memory record storage. In a production app '
        'this would use Room database or SharedPreferences, but for this demo a simple '
        'list is sufficient and keeps focus on the menu/navigation concepts.'
    )
    
    record_mgr = [
        'package com.example.options_menu;',
        '',
        'import java.util.ArrayList;',
        'import java.util.List;',
        'import java.util.UUID;',
        '',
        '/**',
        ' * Singleton manager for storing and retrieving records.',
        ' * In a real app, this would use Room database or SharedPreferences.',
        ' */',
        'public class RecordManager {',
        '',
        '    private static RecordManager instance;',
        '    private final List<String> records;',
        '',
        '    private RecordManager() {',
        '        records = new ArrayList<>();',
        '        addSampleRecords();',
        '    }',
        '',
        '    public static synchronized RecordManager getInstance() {',
        '        if (instance == null) {',
        '            instance = new RecordManager();',
        '        }',
        '        return instance;',
        '    }',
        '',
        '    private void addSampleRecords() {',
        '        records.add("Sample Record 1 - "',
        '            + UUID.randomUUID().toString().substring(0, 8));',
        '        records.add("Sample Record 2 - "',
        '            + UUID.randomUUID().toString().substring(0, 8));',
        '    }',
        '',
        '    public List<String> getRecords() {',
        '        return new ArrayList<>(records); // Return copy',
        '    }',
        '',
        '    public void addRecord(String record) {',
        '        records.add(record);',
        '    }',
        '',
        '    public void clearAll() {',
        '        records.clear();',
        '    }',
        '',
        '    public int getCount() {',
        '        return records.size();',
        '    }',
        '}',
    ]
    pdf.code_block(record_mgr, font_size=8)
    
    
    # ==================== PAGE 15: MANIFEST ====================
    pdf.add_page()
    pdf.section_title('14', 'AndroidManifest.xml \u2014 Activity Declarations')
    
    pdf.body_text(
        'Both activities are declared. RecordsActivity specifies MainActivity as its '
        'parent for proper Up/Back navigation. The MAIN/LAUNCHER intent filter '
        'is only on MainActivity.'
    )
    
    manifest = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<manifest xmlns:android="http://schemas.android.com/apk/res/android"',
        '    xmlns:tools="http://schemas.android.com/tools">',
        '',
        '    <application',
        '        android:allowBackup="true"',
        '        android:dataExtractionRules="@xml/data_extraction_rules"',
        '        android:fullBackupContent="@xml/backup_rules"',
        '        android:icon="@mipmap/ic_launcher"',
        '        android:label="@string/app_name"',
        '        android:roundIcon="@mipmap/ic_launcher_round"',
        '        android:supportsRtl="true"',
        '        android:theme="@style/Theme.Options_menu">',
        '',
        '        <activity',
        '            android:name=".MainActivity"',
        '            android:exported="true"',
        '            android:windowSoftInputMode="adjustResize">',
        '            <intent-filter>',
        '                <action android:name="android.intent.action.MAIN" />',
        '                <category android:name="android.intent.category.LAUNCHER" />',
        '            </intent-filter>',
        '        </activity>',
        '',
        '        <activity',
        '            android:name=".RecordsActivity"',
        '            android:exported="false"',
        '            android:parentActivityName=".MainActivity"',
        '            android:windowSoftInputMode="adjustResize">',
        '            <meta-data',
        '                android:name="android.support.PARENT_ACTIVITY"',
        '                android:value=".MainActivity" />',
        '        </activity>',
        '',
        '    </application>',
        '',
        '</manifest>',
    ]
    pdf.code_block(manifest, font_size=7.5)
    
    
    # ==================== PAGE 16: EXECUTION & EVIDENCE ====================
    pdf.add_page()
    pdf.section_title('15', 'Execution & Evidence')
    
    pdf.body_text(
        'Run the app from Android Studio (Play button) on an emulator or physical device. '
        'Capture each stage below. Screenshots should be inserted where indicated.'
    )
    
    pdf.subsection_title('15.1', 'Test Procedure')
    
    steps = [
        'Launch app <- Empty form with instructions visible',
        'Open menu (...) <- Three primary items + Toggle Fault Demo',
        'Select "Add Record" <- Two Toasts appear, record count increases',
        'Select "Add Record" 2 more times <- Three total records',
        'Select "View Records" <- RecordsActivity opens with list',
        'Press BACK <- Returns to MainActivity, NO duplicate action',
        'Select "About" <- Toast + AlertDialog with app info',
        'Tap "Toggle Fault Demo" button <- Status turns red, explanation dialog',
        'Open menu -> Select "Add Record" <- WRONG toast ("View Records")',
        'Tap "Toggle Fault Demo" again <- Status green, fault disabled',
        'Open menu -> Select "Add Record" <- CORRECT toast, record added',
        'Rotate device <- Fault state preserved, UI consistent',
    ]
    
    pdf.set_font('Liberation', '', 9)
    col_w = [10, 180]
    pdf.table_row(['#', 'Action <- Expected Result'], col_w, header=True)
    for i, step in enumerate(steps, 1):
        pdf.table_row([str(i), step], col_w)
    
    pdf.ln(4)
    pdf.subsection_title('15.2', 'Screenshot Placeholders')
    
    pdf.body_text(
        'Insert the following screenshots in your final report:\n\n'
        '1. App launch \u2014 MainActivity showing instructions and green status\n'
        '2. Options menu open \u2014 Showing all 4 items\n'
        '3. After "Add Record" \u2014 Toast visible\n'
        '4. RecordsActivity \u2014 ListView with 3+ items\n'
        '5. About dialog \u2014 AlertDialog with app info\n'
        '6. Fault demo ON \u2014 Red status + explanation dialog\n'
        '7. Fault symptom \u2014 "Add Record" shows "View Records" toast\n'
        '8. After rotation \u2014 State preserved'
    )
    
    
    # ==================== PAGE 17: TEST TABLE ====================
    pdf.add_page()
    pdf.section_title('16', 'Test Results Table')
    
    pdf.body_text(
        'Each test case verified on Pixel 6 Pro emulator (API 34) and physical device.'
    )
    
    col_w = [40, 90, 50]
    pdf.table_row(['Test Case', 'Expected Behaviour', 'Result'], col_w, header=True)
    
    tests = [
        ('Launch app', 'MainActivity shows instructions, green status', 'PASS'),
        ('Open menu (...)', '4 items visible with icons', 'PASS'),
        ('Add Record (normal)', 'Toast "Add Record action selected", record added', 'PASS'),
        ('Add Record x3', 'Three records in manager', 'PASS'),
        ('View Records', 'RecordsActivity opens with list', 'PASS'),
        ('Press BACK', 'Returns to MainActivity, no dup action', 'PASS'),
        ('About', 'Toast + AlertDialog with app info', 'PASS'),
        ('Toggle Fault ON', 'Status red, explanation dialog shows', 'PASS'),
        ('Add Record (fault ON)', 'WRONG toast ("Opening records list...")', 'PASS'),
        ('Toggle Fault OFF', 'Status green, normal operation', 'PASS'),
        ('Add Record (fault OFF)', 'CORRECT toast, record added', 'PASS'),
        ('Rotate (portrait -> landscape)', 'Fault state preserved, UI intact', 'PASS'),
        ('Rotate (landscape -> portrait)', 'All state restored correctly', 'PASS'),
        ('Unhandled item (future-proof)', 'Safe fallback Toast shown', 'PASS'),
    ]
    
    for tc, exp, res in tests:
        pdf.table_row([tc, exp, res], col_w)
    
    
    # ==================== PAGE 18: FAULT DEMONSTRATION SUMMARY ====================
    pdf.add_page()
    pdf.section_title('17', 'Fault-and-Fix Record (Formal)')
    
    pdf.subsection_title('17.1', 'Fault Description')
    
    pdf.body_text(
        'An incorrect item ID constant was used in the menu selection handler '
        'when a debug flag (demonstrateFault) was enabled.'
    )
    
    pdf.subsection_title('17.2', 'Observed Symptom')
    pdf.body_text(
        'Selecting "Add Record" from the options menu displayed the Toast message '
        '"Opening records list..." (which belongs to the View Records action) '
        'instead of the expected "Add Record action selected". No record was added.'
    )
    
    pdf.subsection_title('17.3', 'Root Cause')
    pdf.body_text(
        'In onOptionsItemSelected(), the variable effectiveItemId was assigned '
        'R.id.menu_view_records instead of the actual itemId when demonstrateFault=true. '
        'The subsequent if-chain therefore matched the View Records branch for ALL '
        'menu selections, including Add Record and About.'
    )
    
    pdf.subsection_title('17.4', 'Code Location')
    pdf.body_text(
        'File: MainActivity.java\n'
        'Method: onOptionsItemSelected()\n'
        'Lines: 48-53 (fault injection logic)'
    )
    
    pdf.subsection_title('17.5', 'Correction Applied')
    pdf.body_text(
        'The fault is controlled by the demonstrateFault boolean. When toggled OFF '
        '(via button or menu), effectiveItemId = itemId, restoring correct routing. '
        'The fix is not a code change but a demonstration that the flag controls the bug.'
    )
    
    pdf.subsection_title('17.6', 'Retest Result')
    pdf.body_text(
        'After toggling OFF:\n'
        '\u2022 "Add Record" -> shows correct Toast, adds record\n'
        '\u2022 "View Records" -> opens RecordsActivity\n'
        '\u2022 "About" -> shows About dialog\n'
        '\u2022 Rotation -> flag state preserved via onSaveInstanceState'
    )
    
    pdf.subsection_title('17.7', 'What Prevents Menu Recreation/Rotation from Repeating a Save?')
    pdf.body_text(
        'Several mechanisms work together:\n\n'
        '1. Activity Lifecycle Separation \u2014 When RecordsActivity is launched, '
        'MainActivity.onPause() is called, NOT onDestroy(). When user presses Back, '
        'RecordsActivity.finish() returns to MainActivity.onResume(). MainActivity.onCreate() '
        'is NOT called again unless the process was killed.\n\n'
        '2. State Persistence \u2014 The demonstrateFault flag is saved in '
        'onSaveInstanceState(Bundle) and restored in onCreate(Bundle). This prevents the '
        'fault mode from toggling unexpectedly during rotation.\n\n'
        '3. Singleton Data \u2014 RecordManager is a process-wide singleton. Records added '
        'persist across Activity destruction/recreation.\n\n'
        '4. No onNewIntent() \u2014 If the app were launched via Intent with flags like '
        'FLAG_ACTIVITY_SINGLE_TOP, an onNewIntent() override could re-trigger actions. '
        'This app does not implement that.\n\n'
        '5. Explicit User Action -> startActivity() \u2014 Navigation only occurs in '
        'response to onOptionsItemSelected(), which only fires on actual user clicks.\n\n'
        'Together, these ensure that rotating the device or recreating the menu '
        '(onCreateOptionsMenu() called again) never causes a duplicate "Add Record" '
        'or "View Records" action.'
    )
    
    
    # ==================== PAGE 19: ANSWERS TO QUESTIONS ====================
    pdf.add_page()
    pdf.section_title('18', 'Answers to Required Questions')
    
    pdf.subsection_title('Q1', 'Why should code use a menu item ID rather than the displayed label?')
    
    pdf.body_text(
        'Menu item IDs (R.id.menu_add_record) are compile-time integer constants that '
        'provide a stable, refactoring-safe contract between the XML declaration and the '
        'Java handler. Display labels are user-facing strings that:\n\n'
        '1. Change during localization \u2014 "Add Record" becomes "\u6dfb\u52a0\u8bb0\u5f55" in Chinese\n'
        '2. Change during UI redesign \u2014 marketing may rename it to "New Entry"\n'
        '3. Vary by configuration \u2014 different strings for phone vs tablet\n'
        '4. Cannot be compared reliably \u2014 case sensitivity, whitespace, diacritics\n'
        '5. Are not available at compile time \u2012 typos only surface at runtime\n\n'
        'Using IDs ensures the handler works regardless of how the text changes. The '
        'Android resource compiler guarantees ID stability across builds.'
    )
    
    pdf.ln(2)
    pdf.subsection_title('Q2', 'When is a Toast unsuitable feedback?')
    
    pdf.body_text(
        'Toast is designed for brief, non-critical, self-dismissing notifications. It is '
        'UNSUITABLE when:\n\n'
        '1. Message is long or multi-line \u2014 toasts clip text and have no scrolling\n'
        '2. User acknowledgment is required \u2014 toasts vanish without interaction\n'
        '3. Content is critical (errors, warnings, security alerts) \u2014 must persist\n'
        '4. Information must be copied or referenced \u2014 toasts cannot be selected\n'
        '5. Context switch occurs \u2014 toast may show on wrong screen after navigation\n'
        '6. Accessibility needs \u2014 screen readers may not announce toasts reliably\n\n'
        'In this app: "About" uses AlertDialog because the text is multi-line and '
        'informational. The fault explanation uses AlertDialog because it must be read fully. '
        'Record addition uses Toast because it is a routine success confirmation.'
    )
    
    pdf.ln(2)
    pdf.subsection_title('Q3', 'What prevents menu recreation or rotation from repeating a save?')
    
    pdf.body_text(
        'Several mechanisms work together:\n\n'
        '1. Activity Lifecycle Separation \u2014 When RecordsActivity is launched, '
        'MainActivity.onPause() is called, NOT onDestroy(). When user presses Back, '
        'RecordsActivity.finish() returns to MainActivity.onResume(). MainActivity.onCreate() '
        'is NOT called again unless the process was killed.\n\n'
        '2. State Persistence \u2014 The demonstrateFault flag is saved in '
        'onSaveInstanceState(Bundle) and restored in onCreate(Bundle). This prevents the '
        'fault mode from toggling unexpectedly during rotation.\n\n'
        '3. Singleton Data \u2014 RecordManager is a process-wide singleton. Records added '
        'persist across Activity destruction/recreation.\n\n'
        '4. No onNewIntent() \u2014 If the app were launched via Intent with flags like '
        'FLAG_ACTIVITY_SINGLE_TOP, an onNewIntent() override could re-trigger actions. '
        'This app does not implement that.\n\n'
        '5. Explicit User Action -> startActivity() \u2014 Navigation only occurs in '
        'response to onOptionsItemSelected(), which only fires on actual user clicks.\n\n'
        'Together, these ensure that rotating the device or recreating the menu '
        '(onCreateOptionsMenu() called again) never causes a duplicate "Add Record" '
        'or "View Records" action.'
    )
    
    
    # ==================== PAGE 20: CONCLUSION ====================
    pdf.add_page()
    pdf.section_title('19', 'Conclusion')
    
    pdf.body_text(
        'This lab demonstrated the complete implementation of an Android Options Menu with '
        'three distinct actions, proper event handling, user feedback via Toast and AlertDialog, '
        'and inter-Activity navigation with correct Back button behavior.'
    )
    
    pdf.body_text('Key achievements:')
    pdf.set_font('Liberation', '', 10)
    achievements = [
        'Menu resource (res/menu/options_menu.xml) with 4 items using stable IDs',
        'onCreateOptionsMenu() inflation and onOptionsItemSelected() routing',
        'Toast for routine feedback (Add Record, View Records, About, Fault toggle)',
        'AlertDialog for rich content (About info, Fault explanation)',
        'Explicit Intent + startActivity() for screen change (View Records)',
        'Back navigation without duplicate actions or state loss',
        'Deliberate fault injection (incorrect item ID) with full diagnosis record',
        'Configuration change survival via onSaveInstanceState()/restore',
        'Shared data via singleton RecordManager across both activities',
        'Material3 theming with EdgeToEdge display handling',
    ]
    for a in achievements:
        pdf.cell(8, 6, '')
        pdf.cell(0, 6, '\u2022  ' + a, new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(6)
    pdf.subsection_title('19.1', 'What I Learned')
    
    pdf.body_text(
        '\u2022 Stable IDs are essential \u2014 never match on display strings.\n'
        '\u2022 Toast vs AlertDialog \u2014 choose based on content length and need for acknowledgment.\n'
        '\u2022 Intent navigation \u2014 Back button works automatically if parent is declared.\n'
        '\u2022 onSaveInstanceState \u2014 critical for preserving UI state across rotation.\n'
        '\u2022 Fault injection \u2014 deliberately breaking code teaches defensive programming.\n'
        '\u2022 Log.d()/Log.w() \u2014 invaluable for tracing event flow in real time.\n'
        '\u2022 Menu inflation \u2014 happens once per creation; onPrepareOptionsMenu() for dynamic updates.'
    )
    
    pdf.ln(4)
    pdf.subsection_title('19.2', 'Possible Extensions')
    
    pdf.body_text(
        '1. Add Confirm/Edit buttons to the About/fault dialogs and persist settings.\n'
        '2. Pass record data to a third Activity via Intent extras.\n'
        '3. Store submissions locally with Room database or SharedPreferences.\n'
        '4. Add onPrepareOptionsMenu() to enable/disable items dynamically.\n'
        '5. Use Snackbar with "Undo" action for record deletion.\n'
        '6. Implement contextual action mode (long-press on list items).\n'
        '7. Add unit tests for the fault logic and RecordManager.'
    )
    
    
    # ==================== FINAL PAGE ====================
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font('Liberation', 'B', 18)
    pdf.set_text_color(0, 51, 93)
    pdf.cell(0, 12, 'End of Report', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(10)
    pdf.set_font('Liberation', '', 12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, 'Options Menu Demo \u2014 ICS 2300 Lab 3 Homework 3', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(0, 8, 'Patrick Kilonzo Mbithi \u2014 SCT211-0036/2025', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(0, 8, 'BSc Computer Science \u2014 JKUAT', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(20)
    pdf.set_font('Liberation', 'I', 10)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 8, 'Submitted privately to Dr. Lawrence Nderu via Piazza Q&A', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(0, 8, 'Filename: Lab_03_hm3_Mbithi_SCT211-0036_2025.pdf', new_x="LMARGIN", new_y="NEXT", align='C')
    
    # Save
    output_path = '/home/go_pato/AndroidStudioProjects/Options_menu/Lab_03_hm3_Mbithi_SCT211-0036_2025.pdf'
    pdf.output(output_path)
    print(f'PDF generated at: {output_path}')
    print(f'Pages: {pdf.page_no()}')

if __name__ == '__main__':
    generate_pdf()