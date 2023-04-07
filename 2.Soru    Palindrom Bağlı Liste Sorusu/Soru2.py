class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
#önceki düğümlerden gelen değerleri herhangi bir yerde saklamalıyız ki bunun bir pandom olduğunu anlayabilelim
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # orta noktayı bularak başlayalıyorum
        cur = head
        N = 0
        while cur:
            N+=1
            cur = cur.next #yani şimdi toplam uzunluğumuz var
        mid = N//2 #orta noktayı buluyorum
        i = 0 #orta noktanın nerede olduğunu takip etmek için burada bir çeşit sayı tutuyorum

        def reverse(head): #buraya ters fonksiyon yazıyorum
            ans = None #bir sonrakini bir yere depolamamız gerekiyor. İlk başta hiç olmayacak çünkü o ilk düğüm artık hiçbir şeyi işaret etmeyecek
            while head: 
                nx = head.next #bir deger varken ne yapcaz
                #sonrakini bir yerde saklayacağız
                head.next = ans#şuan cevapla birlikte öncekine eşit
                ans = head #cevabımızı şu ankinin ne olduğuna göre güncelliyoruz
                head = nx #sakladığımız sonrakine eşit olacak şekilde hareket ettiriyoruz 
            return ans #bir kez yaptığmızda geri dönebilriiz  ve bu bize bağlantılı listemizin yeni başını verecek
        #şimdi birinci ve ikinci işaretcimizi bulmamız gerekcek
        first = second = head # ikinci işaretçimizi orta noktaya kadar hareket ettirelim
        while i<mid:
            second = second.next
            i+=1
        second = reverse(second) #tersine çeviriyoruz bu tabi hala ortada olacak

        while first and second: #birinci ve ikinciye sahipken bu değerlerin hepsinin aynı olup olmadığını kontrol edeceğiz çünkü eğer onlar Bunun bir palindrom olmadığını bilmediğimiz için, 
            if first.val != second.val: return False #eğer ilk nokta değeri ikinci nokta değerine eşit değilse, hemen bir yanlış döndürebiliriz,
            first = first.next #ilk işaretçimizi bir sonrakine
            second = second.next #ve ikinciyi bir sonrakine hareket ettirelim,
        return True