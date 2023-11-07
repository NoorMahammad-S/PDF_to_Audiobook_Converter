# PDF to Audiobook Converter

This PDF to Audiobook Converter Python script allows you to convert a PDF file into speech, effectively creating a free audiobook. It utilizes the iSpeech API for text-to-speech conversion.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- Python 3.x installed
- `requests` and `PyPDF2` libraries installed. You can install them using `pip` as mentioned in the previous instructions.
- An iSpeech API key. You can sign up for one at [iSpeech API](http://www.ispeech.org/api/#introduction).

## Usage

1. Clone this repository or download the script to your local machine.

2. Replace 'YOUR_ISPEECH_API_KEY' in the script with your actual iSpeech API key.

3. Run the script with the following command:

   ```bash
   python pdf_to_audiobook.py
   ```

4. You will be prompted to enter the path to the PDF file you want to convert. Provide the full path to the PDF file.

5. The script will convert the PDF to speech and save the resulting audiobook as an MP3 file.

## Configuration

- You can customize the input PDF file and the output MP3 file path by editing the `pdf_file_path` and `output_mp3_path` variables in the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Please be aware of any terms of use, rate limits, or pricing associated with the iSpeech API or any other TTS service you choose to use.

## Support

If you encounter any issues or have questions, feel free to [open an issue](https://github.com/NoorMahammad-S/pdf-to-audiobook/issues) in this repository.
