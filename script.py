import datetime
import time
from datetime import time as t
import urllib3
import winsound
import requests
import json

listings = []

url_query = "https://d8b22lfluy-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.2)%3B%20Browser%3B%20JS%20Helper%20(3.11.1)%3B%20react%20(18.2.0)%3B%20react-instantsearch%20(6.38.1)"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {

    "Host": "d8b22lfluy-dsn.algolia.net", "Content-Length": "1488", "X-Algolia-Application-Id": "D8B22LFLUY",
    "Content-Type": "application/x-www-form-urlencoded", "X-Algolia-Api-Key": "2d6c7cf80580d79d2b5f31a1908027bb",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",
    "Sec-Ch-Ua-Platform": "Windows", "Accept": "*/*", "Origin": "https://app.rario.com", "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty", "Referer": "https://app.rario.com/", "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9", "Connection": "close"
}

tokens_header = {
    "authority": "app.rario.com", "path": "/api/token-info/xp",
    "scheme": "https", "accept": "*/*", "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,pl;q=0.8,es;q=0.7", "app-device-id": "undefined",
    "app-platform": "website", "app-version": "undefined",
    "content-length": "812", "content-type": "application/json",
    "origin": "https://app.rario.com", "platform": "RARIO", "referer": "",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

payload = '{"requests":[{"indexName":"rario_nft_prod_listing_time_desc","params":"analytics=true&enablePersonalization=true&facetFilters=%5B%5B%22attributes.scarcity%3Ablack%22%2C%22attributes.scarcity%3Agold%22%5D%5D&facets=%5B%22associated_teams%22%2C%22attributes.scarcity%22%2C%22attributes.role%22%2C%22associated_leagues%22%2C%22attributes.nationality%22%2C%22attributes.player%22%2C%22sub_type%22%2C%22attributes.year%22%5D&filters=catalog_type%3Acard%20AND%20on_sale%3A%20true&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=20&maxValuesPerFacet=1000&page=0&query=&tagFilters="},{"indexName":"rario_nft_prod_listing_time_desc","params":"analytics=false&clickAnalytics=false&enablePersonalization=true&facets=attributes.scarcity&filters=catalog_type%3Acard%20AND%20on_sale%3A%20true&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=0&maxValuesPerFacet=1000&page=0&query="}]}'

count = 0

profile_url = "https://app.rario.com/api/users/profile"
cookies1 = {
    "appSession": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwidWF0IjoxNjgzMDAwMDI4LCJpYXQiOjE2ODI2ODk5NzgsImV4cCI6MTY4MzA4NjQyOH0..va8jQ347oq8b8qMT.OFRNsEHPuWykzPvL3cyTGwIhqcCOl8m3Tk4imBZezvKh4DKvcHqD2G5V5uFAJIpBQzB0WTtSznRqfiYfMNGzte6ly0Mvux5p5UbsDaQQ-6CqBHzObyERv4c7q3piX1D2BISXaslTWksZvS-ewREMrbDA1Oa_NUuav-QM24r8UHIHZG23jwGDzrLDiUuc0ponov0i0hQ8V0K3AgsJ9n6j4Voba8c5dnb9oB8X2Ql-WbnVjXO5sbntYbRFv6VeFjsUPnKA-pj2NOFVcUt_fUeniJsKzh15ubNm959OUGMNluhXS13bPyOzrwnG0cGsz0apPdz8hXkByDHnUbhOL8Koi2bhdcNCL1rYL7h812NPaPbXWrAfwdXBPfUCn4kLAciN0_Vn4ZkcAAUdxUBTMxqd919d0dotHCPROI4p7GearymbiOhTRYLFsOUNmI-6LHarhFueQRnrO32jHyo1F7fawvaZ6FuncJLJt6Hi3_658QeZkAZpkgeIKY_Qvjg7mLu2KxXbtej4xqofHbbg3z0OU56rmZ_2qlmC7S7xfLNfEnJyBPhzj7xcA-eYCe1BNwkmz3l7nq64EY32yURMol6NkYRabColUh2bs87tZ7L0zgXcPyE4bayY8mljRf7Fem3LZ4PaPDjrlu_BF9hFdEdwDnd4CJbUDKTUmtXyE0OkZGXJvHSbOwY_JozNhNtKjqVkluMtdCuEUU_hUGrSmrb_vzMu1Uwnfa4FZBry18j6GIffWEMi8_vZYD-Hef_u-LYuPU6sDVHcH3n1LWq9RJI0SWe-0d5xNpJrHWTiV5SZTKJPjFxOaRgS5-K9gX9s8bYNG7IaTh2HF6QgqF8ccTg_JSQN5gQnqz5arjCcuubyBEMbEZjk0hOx8TglIiAmQRKZ7X1j5gDff2eoLPPAy9xTV-BuWHtjXJjbHYEyucvaNu8Qadnv_x5O8WhJhjWY03qv9YrwYek45sXCchAPmDrJKZrfMh7_pBobJ4J24DGUbxXdqtbeunVAusxYqPYIjl-RZxR00xJQr3HVdvUAmQrxBHJ1XoRuiJqMfIQfdGYGKtOfxBGJC2wqjQgr57BL3j1uy0sCxWX7nf-faqWzUIapWF1WvxpwmHoQJKluFePZrY7R10UeHd9YiLTyPKI6OFgx4m3s68HMBN5pYiox9dmcZb7QqHTD9y6nyiJnTd9xExNaVix1lRd2qKED4tCejvLXNGIa-D5A1RAd9Yp8vBGkhJ8O_Zfn-rUEgDavcWxrB7YzkOzZ-BpHQkCyioQo6GB8eU6MXvIk75Fm9BQTcemX7xU4ONXmonIPjXappLjXl33rEbAUl7G_EUpt4E8jxHE8gesY0dTSky9SrwByH40iy29UIld9E60fn_6Yj45DRrk0x5G9IFCv1eB4sAMeTu5ssPzUUksjW3ZuZJ-9whtSwItWGRRrC8C5xFDAJhSXuhc2FzuSKLjZJZ8YUjBQH8xbL2n313xSBdY4Np-4w_2fDaIXSfc5ktERFVg2lFAbDdQSXpi2TH2Cf0v8mLbwkSCiLrW-42SriTK_JP6NXbIzDDOy4oUqtQOZEkdQg4LxZzhR8fQjtgu2Wqj7WLwGi9794B125SuHsi_ZBDoyZGBNipQUgo27ZAxs96FNf8Q-5RwidmGplB3A29hl23dnuyR3xn_29DJPqyg9dxK6WjRXvhNenrdmbKqGsJBeDhv9wUZr-5wwz2GuQdBo-I5mgBUj4B6xQ5FnCRJ77-TC-eXUxLSy8m2nkw8mQrRDmKmPJSxpaIXZouN10HCS4KUIWc45sFao86O5-hxxSPHiFzGKUVp3MIE1p6XkPGObsIE4WAsSmuMIjWtbgbOZwefW1J1P0ygZiDdTJibWm_FIh5cqHLOM_pTNfx3z5aJ2_dCO2ItMCGXvwakxsPySbk3QErJfr0q1S2E9dx_sU1zz4DSQHcrRGJ-gPUug1aY9nkRL_vhk2yUnu1W0SIlMvLjFzNsQwutCzuSPrwyGgnb68pPWzGaZWxOxBY2d5a9UONNu66h74TUILNTH7GN0pLT8QIzFleFJFeH20GaB8xqsq2Yl0Yw9XcxJwjYoMB-gpiAlUgqsdrqIv1m7X4758r621_uXRqvpp3bIfCwR03A0BNluU8rDlLef_cvXkJWk6mkBOuJTfi-HWku4iJPMRT5YK7FYnGmJ24eGKm4Z_aG-7ozzzlhWoIwa7DbFrCP17p95Tt_MZHocU1pvYmMFtJBtEGTH0zprVO0YaftAmU26vZCT8qp2bxqEs9fpDT8nOjzJikd0FnGDeoIEme_D5GJCLrQ2axVKqPWeHBZI1rL_ktVi00H7xLn_9uje0qPs4FWSX2FUPywZBm5fpYDvlK0AHo9nKWSfvG262NRzgvR884dLnI9U5kR6QCiReaPTBIqd0_O0uLRaL5D0as0fwsUc_PGjhZn0DvcBBii9Zg5qEZ8OuDCKONTBIkIShYR9aVKLunfzG4ozLLxw2pnjlXbD3wvSztHGXC1juXE-fOifUHoSWjEhDLoRZtmR2AtitdNwJQZXM9aSuU9cs4Z3IxxTi5KCLLM6dILF6JniVjmT7IUPJ1SIdSP2mlEyX1JvWEs7rJ6xoISJL35jFHjPPvHScMbaOmFmqLgS8Is5rSe_kSdi505vWlCJUPuWYSmcnIeaM-ORncqZlB9JD47QJrQLTEGnT_-D8zjerhMYhHKAfgCajUqyQ_tRtOhrGSeIBYgapn2niyw1dys2JAkEnLIQlvOW1TbLzLtUs56khTXBciszy7Y5aASAl3riGnd5Jcn3gN3T_dg2vBBQyzbTFYSOh6crHhAz635ezWCfWTQXqRG13fDQi61llo-YbBWZd13GbxStPtkzn4oYqPmX7OPMk_yNwVB8Zco1GMNGlNn2YMon3MyrjLhCB61vv6CD1MQU5hcfInzmk-rNanj_5MFrpTftjLTubXjl04c3IqUin29DQ0auYcwyRw8iNfybxzvlWWnJZh-xFV4APtprDg_BgNoCbden794Xq6Y7sUFUG4vAmbIUc87QYmIcL1LrYkv66H3QlrBUo-Eu8ih1aETHUrlydTsFA_AzpU6bLWfwmm-6gnrYyQoRRZ-l-yvsicoQU1NisOWqR6glViDn35o8jG5XFI2ZSvWQK4dfF38KxA6MPl5E9Juii20oTxm3Ewwtosj8RpT9nZ7bt01VINtWtnzXBpmf5XsP8EgdiPzyg7CCMgEMUbRSP6VVbLT9tWjq-YsjcwwL5GWDjHN4gBKw6rDgADB8P7xrjbSl7nMdnss_acCcvXJyykWVlF1kBPoWdFh_UVGdIyY3biNkidRpEXfWN2u1uamIAFB1NVtkQd7L_K_AejSF4GYLFtYxmXbDEOkaSbxiWAiJw_Iwdvb8NE_n5MG7591XR5QkpZm99AcN-m5qfR17vt_YbHrai_pFb97CjaRfV8YEcbAqiEcAhxwjPp4XePHG4fazIPY9loAzOwMj6TzxtPbGQWzemEyjlP914_WWz2G5R4i8CgqLVeaV0Pn8hkRWknwmH8V5BkxxDjUrEsfR0LIrhWnxJZB--JJDh_6JVDJw5NrFSp0GdYCQVKwjwcBDRKjd9-nI.GCNBLXDK5zKSALNAUH7uMw"}
api_session = ""

cookies2 = {
    "appSession": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwidWF0IjoxNjgzMDAwMTAyLCJpYXQiOjE2ODMwMDAwOTIsImV4cCI6MTY4MzA4NjUwMn0..fkjTaG-PTfFaXcjB.fTq-Ez_19EZOAdzQuPLN1OJs0uOnl9ulVdzXGawkSGKiwmkKX6XK2595sggDTWQDemiTOPqFpyxPuLPFO0755HvjL6WwZsdG7OHjXdQoNUndN0vIf-tlAxSU5eBzRsgmRnjrVLRSv4Cdo-OQVLtgdJG3f1HX8p-ePLbkHQ_G9krbZVeZ2kn2twTkd6R-h9ixgsS2dJdD7ULLwITyxmEd4oBo27GYyx7IgVjKm7U12c2neaFcSWRlOscvQEKc57uokIjgw_azEsDe8jAmn_Qg3jmqPvqQmW1r3ZSPwkV2YwlKV38r1c4PhlYG90tFq7ovNU175cy5SrgdS-UUCydV8xXbrlKBCekd03GIDCoWb47kNqdVMR9_msQJkrNJOMEQIl57izUrnU4ICLqVNgQGbPjgP5O3RXFkVUBV7CDoN1VLch_5c7PUSrsit8rxaIUaq5DGEAgyCuU0ke3s9XXW7iOP1C2fp8Z4Ygszr4P-4mwYV2h_qpA_uziBvI5fPlrjCFDqOHgzRou9Jyq3s3VvaCAeW2NJs2D_U3_s1J-UG48hbE75e6kpazBHtXL_kAO0oUzNCsASQIWszM3Xjr7piIuzyDPFbLbxhabRnCCopGhspdL4Z5kP3UOdGbfwpohGQLEoXcaWCARdHLJK-jPhAwZW3HPHGpipsdvQNH_xTaeolkCx9cUlghQiO7wC06MP5kfp3Cr83LnpZI9hwETmkjpQaL6IbDiuSQqzesgMPigKIu4545mKSE9oYxDo5TY0INdlr-_iw3nhTzW5T2DT_bYc8rpm6MEkkTdPNszCzArSgwSfMJ1ynYOlknOw5B_dEcDymjcs6cC5SoeL4B2aZaAbSQe3E261gm99fwZMVav79lbeilkx80HKurrt7rX8UyXgYCFjiQdDeewJS316XYijTQHMwpM6quDVkvGi6nTRsT_HWLZUiLcXgsS3cX_i3jD7w4dsvBfxHUwFfoqOdWZx6eXkylQ-eTSepjBHwH0vgpnon1mFaPi3Nr732Wyzhp8W-IhHbufgMp7Bx7no1Mm0Oh-ifdyxF5T3GqZkqcoRwu-xx_JzawF97ZX2QyGx1Glh9UysxpbXtOvN4DAItI1FTxS8g8fzSr8XswUXDZOXhvmLDauL_dNBV7T_jJTIYLytE0t3_0OmdqnclRyl_AK67H9I5mbDoyuzExOTa6JMic7_GSXbMTV8UT4_j8VNoiRQFljKFZqGDlSM17YClXYIdIcmvUdjJau70uklbSJdyByVjv0AmJSjAbd447tdduRtJjqIKdZDcHUQBHKuLXiJHeCqUBhg8aG9CuhQo0G0Nqfh1BH_87ZZ1fhR7l5WWC7U7QvNRgIm0xKkWXFlxC49OiW922FbfUHOWGGooCWFpWWtagK6QVtZ7z_MtBi6l854t7-0Wlsg_3l9y7j85FJfsyk090oHGTq5mvRDMNqBU6frOwdlkf1FPaam0PHD3AU-LPap9FLHXGd8XXm3TXLSO-zExqgPR788N20I36DnNx-z7EbDFuLr-DudjlH9XDIT5A5IIwHUxtfqwSk2iTII9-ic8o3-hkQuhKlMZRCwVkOKc9FWprLzpKNCcc94_zBzuIirDe4MUDcLzVQllZP6DnrgwvcJu4_JGjBsA9XZRec52ahv1xwYRNEuIG3_5aExjNpDQfCwHh9z1EPTSGf-tx8eueiO3QN5TVemCeU7uZIM9jXDQbThvAjKpHgM9mC1XVK0cFw6P6OtgzskNLBgR-3sDQYfKB9AoCrAVYo9nsXcrafPC166fcrzeX2D4Cd4-_Plody8v567HEhUeuK3Sd6RrOka9qWrfio546NP9I5WLL0D_5h-pJynoCanumXxjf32UsGr8j7UdB63pgA8wblK2MoP_22wlxk02Ta9im8ssCDGq3ohmWIj2n41wkFyTwV5r1009rjwbL3s2qIWK4yIB0LELsTmd_aj5Y1jC4NbGL56k6DduqEdrjQaW7H4Ja0UMdNUi3-Za4Cu355ItJnoP1yxJ1yckWM9YPuGq70s0rpgZe-iA1Rdwdva8aXPmH_o5V_D1DCNwFqQzt8_4PcPaqbTf3yr9g03vHF_L4z5ZaS9UtFlPt5Oq_V3MMIfJVUpw3Kz-CEB6vLxhfwNxikMwv2pC0zo-Ve6NUbZ2OI0iztxvpJ27hMrwx-Jm1hX2dl3db-M39vuJ6elAxRVio5Bx3T2P_2sYn1Sz_Q-f09vGaX1kw8lfDDd9qdG7pr2pZUWymTCaywUJSLhDEW6gCrfMRtzDEd0FLJ1sMQard7-YnVvQfP1_WUPclxqDjdDaW8rmFyjhGIB-q1T97vUqbbKa6obGxvAtskkPOdNkSMun-rQGGCSA9vFJ4K-evSGfnnSinQwa_cV3GUdrF6ftJlVHelrnZzEFC-5Mx9-bIIv3dgPenX8DMgHSD9weW1tKnpytbNJ9Vuev-QjlsaF747-dsDPhK3yJb4vhuJ9O3LFEmtw33RcqHNUER9EcUhWXj3Jk7Ui8lBF7e4UO9K3qk5pvODptfcL87RDPKqIyqs9gtMnJbajoGRqHy85JEYy7IsSXLO_yGNZyakY2dRMa5FuJMovw7z3MdCzFwyL5g2n5iGxFjgq_WKL8aszWhN3w61SMc8ehhn9eM24fd-m_zghUcTS7pou_R7CRY2rNsXKVGqhXTYzm-_ypH-gi8tM6efNzHdi7K8RTK2XSjoduBReGVv2iBs336y8d2DyhWQUCM_xjpJ8sUKYWsVmpxRa1g0_AmnIru5iTkERuWwo172qy5scWfD07Tg3hUtep52tjfSmPT5Ryxib-pdrBc4y3Jdu9AOmk5Au8VVz8_aNMyjJDunNTtLmb7HWkXyRzJbzAKEGN6dxy7oFQYyJrje-4auKwb8pswp0of6RrQnk-PCVG5mGL8lHaRZv161gLGvYue0m1eKqqTTPMgwmYOGTcbzIDQdElrCQSI2rSX-qqdeFx9g2OF052bAvDwfvrzLeA1gGftGDXwKeGXIp6j3FAHnQJbLb-vWG87bOnZZ8fGXp8D5O6e5Sm_dOcBr59iKFgWbU_F_fd3g3eChphjuwoP-IjmvSvH8pg7qC6U9FbmQ0AWMgN4NVK48JfjqGOmRP1YQn12r7uFKZ6MS2J-MGHpto7EzYJiXm8UrjDP2CjbZ59qaQvVOf79ySjrYmoNxCagQg6bVHrkVsQY7fUM7kE2IVb5j5w3kwP6SjiCcqE7nE5l3SNHbvBs6n9u8zLoRNqHEGxdcatG7z39e47hAGva7Rfcc6I4hRVRbntFo5FSoyRi0QnYbcjNvFnNpkl0dkDEZyaj96g-z2WitGdfvlq7q2r4pO0gcZtrjYU_YRcpt-VwXADECCanxGHi9z-jAD5frjwdfGmNDC516r5WGgtegyH4qjOD42TYoijemVZAzlxNqMTpdrYDcqQ5MnqFEwFA8hSPmQiTbQCq6Uyn0wD5aRlJrRJnAIZnHRhFYFzpdiAHZdK9pg-kd9hYpnrK9oL6-ZwBHT5naPBRf-5876Mk-gMStwK6eJaqABkx3B5KuOJc2gcTTkZu8-Wqjlez0vOxA_lyOaV0Os1DVL4Owjd0T2FkrTQ3olCFfoUhzl0KAoMLrRE0YbTpwBzvnvu_9j9xa0DscO0_j5P7Br-c_dunxVIsPiEjBur0CNouQswGLoJLzsGlQjjCfjE9e27OXK77xdQ_3ZhdqEENOUVp2T3fxca8te8UKTQjI.rzw812Ayrhwt3RPvBA_Nzg"
}

list_exceptions = ["Rishi Dhawan", 'Mustafizur Rahman', "Kane Williamson", "Prithvi Shaw", "Bhuvneshwar Kumar",
                   "Litton Das", "Sisanda Magala",
                   "Bhanuka Rajapaksa", "David Willey", "Brendon McCullum", "Ashok Dinda", "Deepak Hooda",
                   "Dhruv Jurel", "Suyash Prabhudessai",
                   "Prabhsimran Singh", "Kuldeep Sen", "Shahbaz Ahmed", "Daren Sammy",
                   "Dwaine Pretorius", "Ravi Bopara", "Mohammad Amir", "Abhinav Manohar", "Harpreet Brar", "Avesh khan",
                   "Dinesh Karthik", "Aaron Finch", "Chetan Sakariya"]
lst_stars = ["Irfan Pathan", "Herschelle Gibbs", "Liam Livingstone", "Arshdeep Singh", "Ruturaj Gaikwad",
             "Maheesh Theekshana", "Moeen Ali", "Cameroon Green", "Ishan Kishan", "Virender Sehwag", "Kusal Mendis", "Kasun Rajitha", "Pathum Nissanka", "Fazalhaq Farooqi",
             "Faf du Plessis", "Glenn Maxwell", "Josh Hazlewood", "Shane Watson", "Yashasvi Jaiswal", "Alex Hales", "James Vince",
             "KL Rahul", "Quinton de Kock", "Jason Holder", "Devon Conway", "David Warner", "Mitchell Marsh",
             "Rashid Khan", "Kyle Mayers", "Mohammed Siraj", "Sachin Tendulkar", "Trent Boult", "Axar Patel", "Brandon King", "Shai Hope",
             "Jason Roy", "Hashim Amla","Anrich Nortje", "Brett Lee", "Phil Salt", "Rovman Powell", "Jofra Archer", "Jason Behrendorff",
             "Heinrich Klaasen", "Marcus Stoinis", "Steven Smith", "Yusuf Pathan", "Shadab Khan", "Babar Azam", "Tim David", "Dewald Brevis",
             "Michael Bracewell", "Lockie Ferguson", "Rahmanullah Gurbaz", "Rahul Tripathi", "Marco Jansen", "Adil Rashid", "Akeal Hosein",
             "Glenn Phillips","Noor Ahmad", "David Miller","Odean Smith", "Alzarri Joseph", "Adam Zampa", "Obed McCoy", "Shimron Hetmyer",
             "Mohammad Hafeez", "Ravi Bishnoi", "RP Singh", "Daryl Mitchell", "Will Young", "Matt Henry", "James Neesham", "Kamran Akmal", "Naveen-ul-Haq","Nicholas Pooran"]


def send_telegram_notification(msg):
    chat_id = "-1001912925595"
    token = "6143122932:AAGuH2HHTrdPvjNkW4VJ34mtOug6n-BtF6Y"
    a = "https://core.telegram.org/bots/api"
    send_message_endpoint = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-981475987"
    url1 = f"api.telegram.org/bot{token}"
    base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.post(base_url, verify=False)


def get_epoch_time(a):
    from datetime import datetime
    date_lst = a.split("T")[0].split("-")
    time_lst = a.split("T")[1].split(".")[0].split(":")

    def timestamp(dt):
        epoch = datetime.utcfromtimestamp(0)
        return (dt - epoch).total_seconds() * 1000.0

    dt = datetime(int(date_lst[0]), int(date_lst[1]), int(date_lst[2]), int(time_lst[0]), int(time_lst[1]),
                  int(time_lst[2]))
    return int(timestamp(dt) / 1000)


def buy_now(url, catalogId, listing_id, name):
    buy_url = "https://app.rario.com/api/loki/users/order"
    buy_headers = {"authority": "app.rario.com", "path": "/api/loki/users/order", "scheme": "https", "accept": "*/*",
                   "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9,pl;q=0.8,es;q=0.7",
                   "app-device-id": "undefined", "app-platform": "website", "app-version": "undefined",
                   "content-length": "58", "content-type": "application/json", "origin": "https://app.rario.com",
                   "platform": "RARIO",
                   "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
                   "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "Windows",
                   "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    buy_headers["referer"] = url
    payload = r'{"catalogId":"<c>","listingId":<l>,"isIndianIP":true}'
    payload = payload.replace("<c>", str(catalogId)).replace("<l>", str(listing_id))
    response = requests.post(buy_url, payload, headers=buy_headers, cookies=cookies2)
    t_data = json.loads(response.text)
    order_id = ""
    try:
        order_id = t_data["data"]["orderId"]
    except Exception as e:
        send_telegram_notification(f"Tried buying got error, {str(e)}")
    send_telegram_notification(f"New Buy option: {url} for {name}  . Order {order_id}")
    time.sleep(5)
    cancel_headers = {"authority": "app.rario.com", "path": "/api/loki/users/order",
                      "scheme": "https", "accept": "*/*",
                      "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9,pl;q=0.8,es;q=0.7",
                      "app-device-id": "undefined", "app-platform": "website", "app-version": "undefined",
                      "content-length": "58", "content-type": "application/json", "origin": "https://app.rario.com",
                      "platform": "RARIO", "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
                      "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "Windows",
                      "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
                      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    # cancel_headers["path"] = f"/api/loki/users/sales/order/group/{order_id}/reconciliation"
    # cancel_headers["referrer"] = url
    # reconciliation = f"https://app.rario.com/api/loki/users/sales/order/group/{order_id}/reconciliation"
    # requests.post(reconciliation, headers=cancel_headers, cookies=cookies2)


def get_listing_details(asset_id, player_id, black_price=151, gold_price=35):
    print(f"Getting listings for asset id {asset_id}")
    listing_url = f"https://app.rario.com/api/token/listing?page=0&limit=30&catalogId={asset_id}&sortBy=price&sortDir=asc"
    resp = requests.get(listing_url, cookies=cookies1)
    response_data = json.loads(resp.text)
    prices_dict = {}
    xp_payload = r'{"tokens":['
    xps = None
    details = []
    for item in response_data["data"]["results"]:
        for k, v in item.items():
            token_id = item["token"]["tokenId"]
            scarcity = item['token']['scarcity']
            if scarcity == 'black':
                min_price = black_price
            else:
                min_price = gold_price
            if k == "token" and int(float(item['price'])) <= min_price:
                prices_dict[str(token_id)] = item["price"]
                prices_dict[str(token_id) + "_listingId"] = item["listingId"]
                mint_time = item["token"]["mintTransferedAt"]
                mint_time = get_epoch_time(mint_time)
                data = r'{"tokenId": "<<token_id>>", "playerId": "<<player_id>>", "scarcity": "<<scarcity>>", "mintTime": <<min_time>>}'
                data = data.replace("<<token_id>>", str(token_id)).replace("<<player_id>>", str(player_id)).replace(
                    "<<scarcity>>", str(scarcity.upper())).replace("<<min_time>>", str(mint_time))
                xp_payload += data
                xp_payload += ","
    if prices_dict:
        if "," == xp_payload[-1]:
            xp_payload = xp_payload[:-1]
        xp_payload += r']}'
        tokens_header["referrer"] = f"https://app.rario.com/listings/{asset_id}"
        url = "https://app.rario.com/api/token-info/xp"
        response_xps = requests.post(url, xp_payload, headers=tokens_header, cookies=cookies1)
        res = json.loads(response_xps.text)
        response_details = res["data"]["nftXps"]
        for each_time in response_details:
            each_time["price"] = int(float(prices_dict[each_time["tokenId"]]))
            each_time["listingId"] = prices_dict[each_time["tokenId"] + "_listingId"]
            details.append(each_time)
    return details


def check_listings(count, listings, dup):
    try:
        response = requests.post(url_query, data=payload, headers=headers, verify=False)
    except:
        print(f"Response code is {response.status_code}. Current time {datetime.datetime.now()}")

        time.sleep(100)
        response = requests.post(url_query, data=payload, headers=headers, verify=False)
    if response.status_code!=200:
        print(f"Response text is {response.text}. Status is {response.status_code}")
        time.sleep(5)
        check_listings(count, listings, dup)

    aa = json.loads(response.text)
    if count % 5000 == 0:
        listings = []
    for lst in aa["results"]:
        for k, v in lst.items():
            if k == "hits":
                for item in v:
                    type_of_card = item["moment_type"]
                    min_price = 151 if type_of_card == "black" else 35
                    if item["min_sale_price"] < min_price and item["name"] not in list_exceptions:
                        player_id = item["player_id"]
                        season = item["attributes"]["year"]
                        asset_id = item['asset_id']
                        current_time = datetime.datetime.now()
                        main_listing_url = f"https://app.rario.com/listings/{asset_id}"
                        data = f" {season} {str(type_of_card).upper()} - {item['min_sale_price']}$ - {item['name']} {main_listing_url}"
                        if data not in listings and data not in dup and item["name"] not in list_exceptions:
                            details = get_listing_details(asset_id, player_id)
                            for each_listing in details:
                                listings.append(data)
                                listing_url = main_listing_url + f"/{each_listing['tokenId']}"
                                data = f"{season} {str(type_of_card).upper()} - {each_listing['xp']}XP - {each_listing['price']}$ - {item['name']} {listing_url}"
                                d_data = f" {each_listing['price']}$  {each_listing['xp']}XP " + listing_url

                                print(f"{current_time}, {data}")
                                if count != 0 and d_data not in dup:
                                    send_telegram_notification(data)
                                dup.append(d_data)
                                if (float(each_listing['xp']) > 40 or (season == 2023 and each_listing['xp'] > 20) and \
                                    item["name"] not in list_exceptions) or (
                                        type_of_card == "black" and item["name"] in lst_stars):
                                    send_telegram_notification(f"Trying to buy : {d_data}")
                                    buy_now(listing_url, asset_id, each_listing["listingId"], item['name'])
                                # if type_of_card =="black":
                                #     frequency = 500  # Set Frequency To 2500 Hertz
                                #     duration = 500  # Set Duration To 1000 ms == 1 second
                                #     # winsound.Beep(frequency, duration)

    return listings, dup


def is_peak_time():
    def is_time_between(begin_time, end_time):
        # If check time is not given, default to current UTC time
        check_time = datetime.datetime.now().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else:  # crosses midnight
            return check_time >= begin_time or check_time <= end_time
    return is_time_between(t(5, 00), t(9, 30)) or is_time_between(t(14, 30), t(4, 00)) or \
           is_time_between(t(18, 00), t(20, 00)) or is_time_between(t(23, 30), t(2, 00))



i = 0
dup = []
listings = []
while True:
    try:
        listings, dup = check_listings(i, listings, dup)
        time.sleep(10)
        if not is_peak_time():
            if i>0 and i%1000==0:
                time.sleep(100)
            elif i>0 and i%10==0:
                time.sleep(1)
        i = i + 1
        print(i)
    except Exception as e:
        send_telegram_notification(f"Error occurred please check code. {e}")
        raise e
