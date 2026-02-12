# def choyxona_qaytim(hisob, tolangan):
#     if tolangan < hisob:
#         return "pul yetarli emas"
#     else:
#         return tolangan - hisob
#
# print(choyxona_qaytim(85000, 100000))
# print(choyxona_qaytim(100000, 85000))


# def qaytim_hisobla(narx, tolangan):
#     if tolangan < narx:
#         return f"pul yetarli emas!"
#     else:
#         return f" {tolangan - narx} so'm"
#
# print(qaytim_hisobla(17000000, 20000000))
# print(qaytim_hisobla(10000000, 9000000))


# def internet_kunlar(mb, kunlik_mb):
#      if kunlik_mb <= 0:
#          return "noto'g'ri qiymat"
#      else:
#          return  mb // kunlik_mb
#
# print(internet_kunlar(3000,5000))
# print(internet_kunlar(5,5))


# def yugurish_statistikasi(masofalar, maqsad_km):
#     bajargan = 0
#     for m in masofalar:
#         if m >= maqsad_km:
#             bajargan += 1
#
#     jami_kun = len(masofalar)
#     bajarmagan = jami_kun - bajargan
#
#     eng_uzoq = max(masofalar) if masofalar else 0
#     ortalama = sum(masofalar) / jami_kun if jami_kun > 0 else 0
#
#     return {
#         "bajargan_kunlar": bajargan,
#         "bajarmagan_kunlar": bajarmagan,
#         "eng_uzoq": eng_uzoq,
#         "ortalama": ortalama,
#     }


