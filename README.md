# Çevre Dostu Discord Botu

Bu proje, çevre dostu yaşam tarzını teşvik eden bir Discord botunu içermektedir. Bot, geri dönüşüm, yeşil yaşam tavsiyeleri, su ve enerji tasarrufu hakkında bilgi sağlar ve çevresel etkinlikler hakkında bilgilendirme yapar.

## Özellikler

- **$merhaba**: Botun kendini tanıttığı komut.
- **$tanit**: Botun amaçlarını ve neler yapabileceğini açıklar.
- **$geri_donusum**: Geri dönüşüm hakkında tavsiyeler verir.
- **$yesil_yasam**: Yeşil yaşam tavsiyeleri sunar.
- **$su_enerji**: Su ve enerji tasarrufu yöntemleri hakkında bilgi verir.
- **$cevresel_etkinlikler**: Çevresel etkinlikler ve kampanyalar hakkında bilgi sağlar.
- **$isler**: Çevre dostu iş seçenekleri hakkında bilgi verir.
- **$yardim**: Mevcut komutlar hakkında bilgi verir.

## Kurulum

1. **Gerekli Kütüphaneler**: `discord.py` kütüphanesini yükleyin.

   pip install discord.py


2. **Bot Token'ı**: Botunuzun token'ını almak için Discord Developer Portal'dan bir uygulama oluşturun ve token'ı kopyalayın. Token'ınızı aşağıdaki satırda yer alan `"token"` ile değiştirin.


   bot.run("YOUR_BOT_TOKEN_HERE")


## Kullanım

1. **Botu Başlatma**: Botu başlatmak için Python dosyanızı çalıştırın.


2. **Komutlar**:
   - `$merhaba`: Bot size merhaba der.
   - `$tanit`: Botun kendini tanıttığı bilgileri gösterir.
   - `$geri_donusum`: Geri dönüşüm hakkında ipuçları verir.
   - `$yesil_yasam`: Yeşil yaşam tavsiyeleri sağlar.
   - `$su_enerji`: Su ve enerji tasarrufu hakkında bilgi verir.
   - `$cevresel_etkinlikler`: Çevresel etkinlikler hakkında bilgi verir.
   - `$isler`: Çevre dostu iş seçeneklerini listeler.
   - `$yardim`: Tüm komutlar hakkında bilgi verir.

## Botun Özelleştirilmesi

1. **Yeni Komutlar Ekleme**: Komutları eklemek veya değiştirmek için, `bot.py` dosyasına yeni komut fonksiyonları ekleyin. Her komut, `@bot.command()` dekoratörü ile tanımlanmalıdır.

2. **Bilgi İçeriğini Güncelleme**: Bilgi metinlerini güncellemek için, ilgili komut fonksiyonlarının içindeki `await ctx.send()` fonksiyonlarının içeriklerini düzenleyin.

3. **Botu Yeniden Başlatma**: Yapılan değişikliklerin uygulanabilmesi için botu yeniden başlatın.
