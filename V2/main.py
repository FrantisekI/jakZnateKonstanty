from flask import Flask, render_template, url_for, request, jsonify
from requests import get
import json
import datetime
from database import conectToDB, addRow, getRows


GpiNaCoZna = GPlaceholder_Pi = GeNaCoZna = GPlaceholder_E = GfiNaCoZna = GPlaceholder_Fi = 0
Gjmeno = 'Anonym'
Gconn, GMeinCursor = conectToDB()


app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

@app.route("/konstanty", methods=['GET', 'POST'])
def konstanty(jakSeJmenuje='Anonym', Placeholder_Pi=0, piNaCoZna='3,', Placeholder_E=0, eNaCoZna='2,', Placeholder_Fi=0, fiNaCoZna='1,'):
    global GpiNaCoZna, GPlaceholder_Pi, GeNaCoZna, GPlaceholder_E, GfiNaCoZna, GPlaceholder_Fi, Gjmeno
    if request.method == 'POST':
        jakSeJmenuje = request.form.get('placeholderJmeno')
        Placeholder_Pi = request.form.get('znalost_PI')
        piNaCoZna, Placeholder_Pi = get_pi(Placeholder_Pi)
        
        Placeholder_E = request.form.get('znalost_E')
        eNaCoZna, Placeholder_E = get_e(Placeholder_E)
        
        Placeholder_Fi = request.form.get('znalost_FI')
        fiNaCoZna, Placeholder_Fi = get_fi(Placeholder_Fi)

        GpiNaCoZna = piNaCoZna
        GPlaceholder_Pi = int(Placeholder_Pi)
        GeNaCoZna = eNaCoZna
        GPlaceholder_E = int(Placeholder_E)
        GfiNaCoZna = fiNaCoZna
        GPlaceholder_Fi = int(Placeholder_Fi)
        Gjmeno = jakSeJmenuje[:250]



            
    return render_template("konstanty.html", napis='Vítej, mohl bych tě poprosit o vyplnění následujícího "dotazníku"?',
                           placeholderJmeno=jakSeJmenuje, tvojeIP=get_ip(), 
                           placeholderPI=Placeholder_Pi, PI_naXmist=piNaCoZna, 
                           placeholderE=Placeholder_E, E_naXmist=eNaCoZna, 
                           placeholderFI=Placeholder_Fi, FI_naXmist=fiNaCoZna)

def get_pi(Placeholder_Pi):
    pi = '3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989'
    kolikJeMezer = int(Placeholder_Pi)/10
    piNaCoZna = pi[:int(Placeholder_Pi) + 2 + int(kolikJeMezer)]
    
    if int(Placeholder_Pi) > 1000:
        piNaCoZna = pi + " ...dál to už neumím :D (já = kód)"
    elif int(Placeholder_Pi) < 0:
        piNaCoZna = "takhle paměť opravu nefunguje :|"

    return piNaCoZna, Placeholder_Pi


def get_e(Placeholder_E):
    e = '2,7182818284 5904523536 0287471352 6624977572 4709369995 9574966967 6277240766 3035354759 4571382178 5251664274 2746639193 2003059921 8174135966 2904357290 0334295260 5956307381 3232862794 3490763233 8298807531 9525101901 1573834187 9307021540 8914993488 4167509244 7614606680 8226480016 8477411853 7423454424 3710753907 7744992069 5517027618 3860626133 1384583000 7520449338 2656029760 6737113200 7093287091 2744374704 7230696977 2093101416 9283681902 5515108657 4637721112 5238978442 5056953696 7707854499 6996794686 4454905987 9316368892 3009879312 7736178215 4249992295 7635148220 8269895193 6680331825 2886939849 6465105820 9392398294 8879332036 2509443117 3012381970 6841614039 7019837679 3206832823 7646480429 5311802328 7825098194 5581530175 6717361332 0698112509 9618188159 3041690351 5988885193 4580727386 6738589422 8792284998 9208680582 5749279610 4841984443 6346324496 8487560233 6248270419 7862320900 2160990235 3043699418 4914631409 3431738143 6405462531 5209618369 0888707016 7683964243 7814059271 4563549061 3031072085 1038375051 0115747704 1718986106 8739696552 1267154688 9570350354'
    kolikJeMezer = int(Placeholder_E)/10
    eNaCoZna = e[:int(Placeholder_E) + 2 + int(kolikJeMezer)]
    
    if int(Placeholder_E) > 1000:
        eNaCoZna = e + " ...dál to už nevím, přišlo mi zbitečné to sem dávat :D"
    elif int(Placeholder_E) < 0:
        eNaCoZna = "takhle paměť opravu nefunguje :|"

    return eNaCoZna, Placeholder_E


def get_fi(Placeholder_Fi):
    fi = '1,6180339887 4989484820 4586834365 6381177203 0917980576 2862135448 6227052604 6281890244 9707207204 1893911374 8475408807 5386891752 1266338622 2353693179 3180060766 7263544333 8908659593 9582905638 3226613199 2829026788 0675208766 8925017116 9620703222 1043216269 5486262963 1361443814 9758701220 3408058879 5445474924 6185695364 8644492410 4432077134 4947049565 8467885098 7433944221 2544877066 4780915884 6074998871 2400765217 0575179788 3416625624 9407589069 7040002812 1042762177 1117778053 1531714101 1704666599 1466979873 1761356006 7087480710 1317952368 9427521948 4353056783 0022878569 9782977834 7845878228 9110976250 0302696156 1700250464 3382437764 8610283831 2683303724 2926752631 1653392473 1671112115 8818638513 3162038400 5222165791 2866752946 5490681131 7159934323 5973494985 0904094762 1322298101 7261070596 1164562990 9816290555 2085247903 5240602017 2799747175 3427775927 7862561943 2082750513 1218156285 5122248093 9471234145 1702237358 0577278616 0086883829 5230459264 7878017889 9219902707 7690389532 1968198615 1437803149 9741106926 0886742962 2675756052 3172777520 3536139362'
    kolikJeMezer = int(Placeholder_Fi)/10
    fiNaCoZna = fi[:int(Placeholder_Fi) + 2 + int(kolikJeMezer)]
    
    if int(Placeholder_Fi) > 1000:
        fiNaCoZna = fi + " ...dál to už nevím, přišlo mi zbitečné to sem dávat :D"
    elif int(Placeholder_Fi) < 0:
        fiNaCoZna = "takhle paměť opravu nefunguje :|"

    return fiNaCoZna, Placeholder_Fi


def get_ip():
    ip = get('https://api.ipify.org').text
    return ip


@app.route("/submit", methods=['POST'])
def submit():
    global GpiNaCoZna, GPlaceholder_Pi, GeNaCoZna, GPlaceholder_E, GfiNaCoZna, GPlaceholder_Fi, Gjmeno, Gconn, GMeinCursor
    addRow(GMeinCursor, Gconn, Gjmeno, GPlaceholder_Pi, GPlaceholder_E, GPlaceholder_Fi, get_ip())

    #print(getRows(GMeinCursor))

    return render_template("konstanty.html", napis='Děkuji za vyplnění dotazníku!',
                           placeholderJmeno=Gjmeno, tvojeIP=get_ip(), 
                           placeholderPI=GPlaceholder_Pi, PI_naXmist=GpiNaCoZna, 
                           placeholderE=GPlaceholder_E, E_naXmist=GeNaCoZna, 
                           placeholderFI=GPlaceholder_Fi, FI_naXmist=GfiNaCoZna)






if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True, host='0.0.0.0')
    

