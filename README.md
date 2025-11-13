# Clinical Biochemistry Utilities

This repository currently contains:

- `viral_replication.html`: a self-contained study sheet that explains the viral replication cycle.
- `student_result_app.py`: a Streamlit application that lets students look up their practical grade from the accompanying Excel sheet.
- `run_viral_replication.py`: a small helper that serves the HTML reference so you can view it in a browser with one command.

## Viewing the viral replication page

1. Install the standard library-only requirements (no extra packages are needed).
2. Run the helper:

   ```bash
   python run_viral_replication.py
   ```

   The script starts a local HTTP server on <http://127.0.0.1:8000/viral_replication.html> and attempts to open your default browser automatically. Pass `--no-browser` if you only want the server.

3. Press `Ctrl+C` in the terminal to stop the server when you are finished.

## Running the student results application

1. Install the dependencies listed in `requirements.txt`.
2. Start the Streamlit app:

   ```bash
   streamlit run student_result_app.py
   ```

3. Provide the registration number in the input box to view the student result that is stored inside `قائمة_الطلبة_ML661_ربيع 2025.xlsx`.
