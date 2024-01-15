// Generate.js

import {
  GenerativenessClient,
  GenerateResponse,
  TranslateResponse,
  WriteDifferentFormatsResponse,
} from "@google-cloud/generative-ai";

// API Anahtarı (HTML dosyanızdaki ile aynı olmalıdır)
const apiKey = "AIzaSyAvDQjTto-gFHfGNw2uA_Nf8Xaf9MLr1Pg";

// Model
const model = new GenerativenessClient(apiKey, "gemini-pro");

// Metin oluşturma
const generateText = async (topic) => {
  const response = await model.generate_text({
    topic: topic,
  });

  return response.text;
};

// Çeviri yapma
const translate = async (sourceLanguage, targetLanguage, text) => {
  const response = await model.translate({
    source_language: sourceLanguage,
    target_language: targetLanguage,
    text: text,
  });

  return response.translation;
};

// Farklı formatlarda yazma
const writeDifferentFormats = async (text) => {
  const response = await model.write_different_formats({
    text: text,
  });

  return response.formats;
};

// Exportlar (HTML dosyanızdaki script'te bu fonksiyonları kullanabilirsiniz)
export {
  generateText,
  translate,
  writeDifferentFormats,
};
