import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.LiveSpeechRecognizer;

public class SpeechToText {

    public static void main(String[] args) throws Exception {
        // Create a configuration with the path to the acoustic and language model files
        Configuration configuration = new Configuration();

        // Set the path to the acoustic model (can be downloaded from CMU Sphinx website)
        configuration.setAcousticModelPath("path/to/acoustic/model");

        // Set the path to the language model (can be downloaded from CMU Sphinx website)
        configuration.setDictionaryPath("path/to/dictionary");
        configuration.setLanguageModelPath("path/to/language/model");

        // Create a LiveSpeechRecognizer with the given configuration
        LiveSpeechRecognizer recognizer = new LiveSpeechRecognizer(configuration);

        System.out.println("Listening... Press Ctrl+C to exit.");

        // Start recognition
        recognizer.startRecognition(true);

        // Continuously recognize and print the recognized speech
        while (true) {
            String result = recognizer.getResult().getHypothesis();
            if (result != null) {
                System.out.println("Recognized: " + result);
            }
        }
    }
}
