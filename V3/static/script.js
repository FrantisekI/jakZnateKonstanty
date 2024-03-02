/* Add "https://api.ipify.org?format=json" to 
        get the IP Address of user*/
$(document).ready(() => {
    $.getJSON("https://api.ipify.org?format=json",
        function (data) {

            // Displayin IP address on screen
            //$("#gfg").html(data.ip);

            const ip = data.ip;
            const url = `/api/ip?${ip}`;
            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ ip }),
            })
                .then((r) => r.json()).catch((error) => {
                    console.error("Error sending IP address:", error);
                    // Handle the error here, e.g., display an error message to the user
                });
        })
});

function decrementValue(inputElementId) {
    const inputElement = document.getElementById(inputElementId);
    let currentValue = parseInt(inputElement.value);
    currentValue--;
    inputElement.value = currentValue;
}

function incrementValue(inputElementId) {
    const inputElement = document.getElementById(inputElementId);
    let currentValue = parseInt(inputElement.value);
    currentValue++;
    inputElement.value = currentValue;
}

function getConst(konstanta) {
    let cislo = '';
    if (konstanta === 'pi') {
        cislo = '3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989';
    } else if (konstanta === 'e') {
        cislo = '2,7182818284 5904523536 0287471352 6624977572 4709369995 9574966967 6277240766 3035354759 4571382178 5251664274 2746639193 2003059921 8174135966 2904357290 0334295260 5956307381 3232862794 3490763233 8298807531 9525101901 1573834187 9307021540 8914993488 4167509244 7614606680 8226480016 8477411853 7423454424 3710753907 7744992069 5517027618 3860626133 1384583000 7520449338 2656029760 6737113200 7093287091 2744374704 7230696977 2093101416 9283681902 5515108657 4637721112 5238978442 5056953696 7707854499 6996794686 4454905987 9316368892 3009879312 7736178215 4249992295 7635148220 8269895193 6680331825 2886939849 6465105820 9392398294 8879332036 2509443117 3012381970 6841614039 7019837679 3206832823 7646480429 5311802328 7825098194 5581530175 6717361332 0698112509 9618188159 3041690351 5988885193 4580727386 6738589422 8792284998 9208680582 5749279610 4841984443 6346324496 8487560233 6248270419 7862320900 2160990235 3043699418 4914631409 3431738143 6405462531 5209618369 0888707016 7683964243 7814059271 4563549061 3031072085 1038375051 0115747704 1718986106 8739696552 1267154688 9570350354';
    } else if (konstanta === 'fi') {
        cislo = '1,6180339887 4989484820 4586834365 6381177203 0917980576 2862135448 6227052604 6281890244 9707207204 1893911374 8475408807 5386891752 1266338622 2353693179 3180060766 7263544333 8908659593 9582905638 3226613199 2829026788 0675208766 8925017116 9620703222 1043216269 5486262963 1361443814 9758701220 3408058879 5445474924 6185695364 8644492410 4432077134 4947049565 8467885098 7433944221 2544877066 4780915884 6074998871 2400765217 0575179788 3416625624 9407589069 7040002812 1042762177 1117778053 1531714101 1704666599 1466979873 1761356006 7087480710 1317952368 9427521948 4353056783 0022878569 9782977834 7845878228 9110976250 0302696156 1700250464 3382437764 8610283831 2683303724 2926752631 1653392473 1671112115 8818638513 3162038400 5222165791 2866752946 5490681131 7159934323 5973494985 0904094762 1322298101 7261070596 1164562990 9816290555 2085247903 5240602017 2799747175 3427775927 7862561943 2082750513 1218156285 5122248093 9471234145 1702237358 0577278616 0086883829 5230459264 7878017889 9219902707 7690389532 1968198615 1437803149 9741106926 0886742962 2675756052 3172777520 3536139362';
    }
    const field = document.getElementById(konstanta);
    const hodnotaKonstanty = document.getElementById(konstanta + '_hodnota');
    const kolikzna = field.value;
    const kolikJeMezer = parseInt(kolikzna) / 10;

    let ConNaCoZna = cislo.slice(0, parseInt(kolikzna) + 2 + parseInt(kolikJeMezer));

    if (parseInt(kolikzna) > 1000) {
        ConNaCoZna = cislo + " ...dál to už neumím :D (já = kód)";
    } else if (parseInt(kolikzna) < 0) {
        ConNaCoZna = "takhle paměť opravu nefunguje :|";
    }

    hodnotaKonstanty.innerHTML = ConNaCoZna;
}



function submit() {

    const jakSeJmenuje = document.getElementById('jmeno').value;
    const pamatovani_Pi = document.getElementById('pi').value;
    const pamatovani_E = document.getElementById('e').value;
    const pamatovani_Fi = document.getElementById('fi').value;
    const zprava = document.getElementById('zprava');
    const Gjmeno = jakSeJmenuje.substring(0, 250);
    zprava.innerHTML = 'Děkuji za vyplnění dotazníku!';
    const data = {
        Gjmeno,
        pamatovani_Pi,
        pamatovani_E,
        pamatovani_Fi
    };

    dataJson = JSON.stringify(data);
    console.log('data:', dataJson);
    const url = `/submit?${dataJson}`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: dataJson
    })
        .then((response) => response.json())
        .then((result) => {
            console.log('Data submitted successfully:', result);
            // Handle the result here, e.g., display a success message to the user
        })
        .catch((error) => {
            //console.error('Error submitting data my:', error);
            console.log('error při odesílání, ale nějak to funguje => nebudeme to řešit')
            // Handle the error here, e.g., display an error message to the user
        });


    /*fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then((r) => r.json()).catch((error) => {
            console.error("Error sending IP address:", error);
            // Handle the error here, e.g., display an error message to the user
        });*/
}



