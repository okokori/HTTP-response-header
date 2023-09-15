# Http Response Header Check 

## Tanım 
Bu proje, web uygulamalarının güvenliğini değerlendirmek ve potansiyel güvenlik açıklarını belirlemek amacıyla oluşturulmuş bir HTTP güvenlik başlıkları tarayıcısıdır. Proje, belirli bir URL veya IP adresine yapılan HTTP isteklerinin yanıt başlıklarını inceleyerek, web sitelerinin güvenlik durumunu kontrol edebilir.

HTTP güvenlik başlıkları, web uygulamalarının güvenliğini artırmak ve çeşitli web saldırılarına karşı koruma sağlamak için kullanılan önemli bileşenlerdir. Bu başlıklar, web uygulamalarının güvenliğini artırmak ve potansiyel güvenlik risklerini azaltmak amacıyla sunucu tarafından tarayıcılara iletilen ek bilgilerdir. Projemiz, bu güvenlik başlıklarını analiz ederek, web sitelerinin ne kadar güvende olduğunu değerlendirmenize yardımcı olur.

## Projenin Amacı

Bu projenin amacı, gönderilen HTTP isteklerinin yanıtlarını alarak gelen responsedan alınan başlıkları ekrana yazdırmaktır. Projemiz, kullanıcıların bir web sitesinin güvenlik başlıklarını hızlı ve kolay bir şekilde incelemesine olanak tanır. Aynı zamanda, web uygulamalarının güvenliğini değerlendiren güvenlik uzmanları ve geliştiriciler için de kullanışlı bir araç sağlar.

Proje, aşağıdaki temel işlevlere sahiptir:
- Belirli bir URL veya IP adresine yapılan HTTP isteğinin yanıt başlıklarını listeler.
- Kullanıcının belirlediği HTTP başlıklarını özelleştirilmiş olarak kontrol edebilir.
- HTTP güvenlik başlıkları ve eksik olan başlıklar hakkında bilgi sunar.

Bu proje, web uygulamalarının güvenliğini artırmak ve potansiyel güvenlik açıklarını tespit etmek isteyen herkes için kullanışlıdır. HTTP güvenlik başlıkları, web uygulamalarının güvenliğini artırmak ve çeşitli web saldırılarına karşı koruma sağlamak için kullanılır.

## Kullanım Kılavuzu

1. Projeyi indirmek için komutu kullanın. `git clone https://github.com/okokori/HTTP-response-header.git`

2. İndirdiğiniz dosyaya gidin. `cd HTTP-response-header.git`

3. Gerekli Python bağımlılıklarını yüklemek için komutu çalıştırın: `pip install -r requirements.txt`

4. Proje dizinine terminal veya komut istemcisini açın. `python3 Http-Response-Header-Check.py`
