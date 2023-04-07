# 2.Soru-Palindrom-Bagli-Liste
2.Soru  :  Palindrom Bağlı Liste. 
Tek bağlantılı bir liste verildiğinde head, eğer bir palindrom ise  true  veya başka türlü ise false döner örnek olarak şöyle diyim :

1->2->2->1
[1,2,2,1] 
çıkış = doğru 

1->2
[1,2]
çıkış = yanlış 

yani aslında döngü mantığı işte tekrar varsa true yoksa false 

-> bağlantılı listenin ortasını alın.
-> bağlantılı listenin sonraki yarısını ters çevirin.
-> sonraki yarı (geri dönüşten sonra) ilk yarıya eşitse
bağlantılı listenin palindrom olduğu anlamına gelir.

aslında basit olarak bu mantığı kullandım kodu yazarken
