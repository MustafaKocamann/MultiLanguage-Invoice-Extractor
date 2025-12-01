# 📄 MultiLanguage Invoice Extractor
Akıllı Fatura Analizi · Streamlit + Gemini 2.5 Flash
🔗 Live Demo:
👉 https://multilang-invoice-ai.streamlit.app/

## 🚀 Proje Özeti
* MultiLanguage Invoice Extractor, kullanıcıların yüklediği çok dilli (TR/EN) fatura görsellerini analiz eden bir yapay zeka uygulamasıdır.
* Google Gemini 2.5 Flash modeli sayesinde:
* Satıcı (Seller)
* Alıcı (Buyer / Bill-To)
* Fatura numarası
* Tarihler (Issue Date, Due Date)
* Para birimi
* Hizmet/ürün satırları
* Ara toplam, vergiler, genel toplam gibi bilgileri otomatik olarak çıkarır. Uygulama, kullanıcı tarafından yöneltilen sorulara görsel fatura üzerinden doğrudan ve anlamlı yanıtlar üretir.
* Web arayüzü Streamlit ile geliştirilmiştir.

## 🛠️ Kullanılan Teknolojiler
* Teknoloji	Açıklama
* Python 3.x	Projenin geliştirildiği dil
* Streamlit	Web arayüzü
* Pillow (PIL)	Görsel dosya işleme
* Google Gemini 2.5 Flash	Görüntü + metin işleyen multimodal LLM
* dotenv	API anahtarı yönetimi

## 🤖 Model Çalışma Mantığı
* Gemini 2.5 Flash multimodal yapısı sayesinde:
* OCR + Semantik analiz bir arada çalışır
* Görselden metin çıkarılır
* Metin içindeki ilişkiler (buyer, seller, totals, dates) anlaşılır
* Kullanıcının sorusu bağlama göre cevaplanır

## 📌 Özellikler
* ✔ Çok dilli fatura desteği (Türkçe + İngilizce)
* ✔ Görsel tabanlı içerik çıkarımı
* ✔ Gerçek zamanlı soru-cevap
* ✔ Streamlit ile kolay kullanım
* ✔ Her türlü fatura formatına uyumlu
* ✔ AI tabanlı otomatik anlamlandırma
