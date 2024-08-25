import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

# Tanit komutunu tanımlıyoruz
@bot.command()
async def tanit(ctx):

    await ctx.send(f'Ben {bot.user}, çevreye duyarlı bir Discord botuyum. Amacım, çevre dostu uygulamalar konusunda sizi bilgilendirmek, atıkları azaltmanın yollarını paylaşmak ve sürdürülebilir bir yaşam tarzına katkıda bulunmak. 🌱\n\n'
                   'Neler Yapabilirim?\n\n'
                   '♻️ Geri Dönüşüm Rehberi: Size geri dönüşüm kuralları ve ipuçları hakkında bilgi verebilirim.\n'
                   '🌿 Yeşil Yaşam Tavsiyeleri: Günlük hayatta daha sürdürülebilir olmanın yollarını sunabilirim.\n'
                   '💧 Su ve Enerji Tasarrufu: Su ve enerji tüketimini nasıl azaltabileceğinizi anlatabilirim.\n'
                   '🌍 Çevresel Etkinlikler: Çevre ile ilgili yaklaşan etkinlikler ve kampanyalar hakkında sizi bilgilendirebilirim.\n\n'
                   'Eğer çevre dostu bir yaşam tarzı benimsemek ve gezegenimiz için küçük ama önemli adımlar atmak istiyorsanız, ben buradayım! Her sorunuzda, her bilgi ihtiyacınızda bir tık uzağınızdayım.')

@bot.command()
async def geri_donusum(ctx):
    geri_donusum_tavsiyeleri = """
    ♻️ **Geri Dönüşüm Rehberi:**
    - Plastik, kağıt, metal ve cam gibi geri dönüştürülebilir malzemeleri ayrı ayrı biriktirin.
    - Üzerinde yiyecek artığı bulunan ambalajları temizleyin, aksi takdirde geri dönüşüm sürecini engelleyebilir.
    - Tek kullanımlık plastikleri mümkün olduğunca az kullanmaya çalışın.
    - Elektronik atıklarınızı e-atık toplama noktalarına teslim edin.
    """
    await ctx.send(geri_donusum_tavsiyeleri)

@bot.command()
async def yesil_yasam(ctx):
    yesil_yasam_tavsiyeleri = """
    🌿 **Yeşil Yaşam Tavsiyeleri:**
    - Kendi alışveriş çantanızı yanınızda taşıyarak plastik poşetlerden kaçının.
    - Enerji tasarruflu ampuller kullanın.
    - İkinci el eşyalar alın veya geri dönüştürülmüş malzemelerden yapılmış ürünleri tercih edin.
    - Çevre dostu temizlik ürünleri kullanın.
    """
    await ctx.send(yesil_yasam_tavsiyeleri)

@bot.command()
async def su_enerji(ctx):
    su_enerji_tavsiyeleri = """
    💧 **Su ve Enerji Tasarrufu:**
    - Dişlerinizi fırçalarken musluğu kapatın.
    - Duş sürenizi kısaltın.
    - Enerji verimliliği yüksek ev aletleri kullanın.
    - Elektronik cihazlarınızı kullanılmadığında tamamen kapatın.
    """
    await ctx.send(su_enerji_tavsiyeleri)

@bot.command()
async def cevresel_etkinlikler(ctx):
    etkinlikler = """
    🌍 **Çevresel Etkinlikler:**
    - 5 Haziran Dünya Çevre Günü etkinliklerini kaçırmayın!
    - Yerel topluluğunuzda düzenlenen ağaç dikme kampanyalarına katılın.
    - Plaj temizleme etkinliklerine katılarak doğaya katkıda bulunun.
    - Çevre bilinci artırma seminerleri ve webinarlara katılın.
    """
    await ctx.send(etkinlikler)

@bot.command()
async def isler(ctx):
    isler_listesi = """
    🌱 **Çevre Dostu İşler:**
    - **Geri Dönüşüm Görevlisi:** Geri dönüşüm merkezlerinde çalışarak atık malzemelerin ayrılmasına ve geri dönüşüm süreçlerine katkıda bulunun.
    - **Çevre Danışmanı:** Firmalara çevre dostu politikalar geliştirme konusunda danışmanlık yapın.
    - **Sürdürülebilir Enerji Uzmanı:** Yenilenebilir enerji kaynaklarını araştırarak ve projeler geliştirerek enerji tasarrufuna katkı sağlayın.
    - **Organik Tarım Çiftçisi:** Kimyasal kullanımını minimize eden ve doğal süreçleri destekleyen organik tarım yöntemlerini uygulayın.
    - **Su Yönetimi Uzmanı:** Su kaynaklarının etkin ve sürdürülebilir bir şekilde yönetilmesi için stratejiler geliştirin.
    """
    await ctx.send(isler_listesi)


@bot.command()
async def yardim(ctx):
    yardim_komutlari = """
    - **$isler:** Cevre dostu isler onerilir. 
    - **$cevresel_etkinlikler:** Yapabileceginiz yararli etkinlikleri onerir.
    - **$su_enerji:** Su ve enerji tasaruf yontemleri.
    - **$yesil_yasam:** Dunyayi daha saglikli yapmak icin tavsiyeler.
    - **$geri_donusum:** Nasil geri donusum yapilir?.
    - **$tanit:** Bot kendisini tanitir
    - **$merhaba:** Kod buna karsilik verir.
    """
    await ctx.send(yardim_komutlari)

@bot.command()
async def gazlar(ctx):
    hava_gazlari = """
    🌫️ **Hava Gazları ve Özellikleri:**

    - **Karbon Dioksit (CO2):**
      - **Yüzde:** Atmosferin yaklaşık %0.04'ü.
      - **Yararları:** Bitkiler fotosentez için kullanır.
      - **Zararları:** Küresel ısınmaya neden olur.

    - **Oksijen (O2):**
      - **Yüzde:** Atmosferin yaklaşık %21'i.
      - **Yararları:** Tüm aerobik canlılar için yaşamsal öneme sahiptir.
      - **Zararları:** Yüksek konsantrasyonlar oksidatif stres yaratabilir.

    - **Azot (N2):**
      - **Yüzde:** Atmosferin yaklaşık %78'i.
      - **Yararları:** Kimyasal reaksiyonlarda az reaktiftir, atmosferin stabilitesine katkıda bulunur.
      - **Zararları:** Düşük seviyelerde oksijen taşıma kapasitesini etkileyebilir.

    - **Metan (CH4):**
      - **Yüzde:** Atmosferde çok düşük konsantrasyonda bulunur.
      - **Yararları:** Doğal gaz olarak enerji kaynağı olarak kullanılır.
      - **Zararları:** Küresel ısınmayı hızlandıran güçlü bir sera gazıdır.

    - **Ozon (O3):**
      - **Yüzde:** Atmosferde düşük konsantrasyonda bulunur.
      - **Yararları:** UV ışınlarını emerek dünya yüzeyini korur.
      - **Zararları:** Troposferde (yüzey seviyesinde) hava kirliliğine ve sağlık sorunlarına yol açabilir.
    """
    await ctx.send(hava_gazlari)


bot.run("token")
