window.onload = function(){
        const img1 = document.getElementById('img1');
        const img2 = document.getElementById('img2');
        const img3 = document.getElementById('img3');
        const img4 = document.getElementById('img4');
        const img5 = document.getElementById('img5');
        const img6 = document.getElementById('img6');
        img1.addEventListener('click', selectimg);
        img2.addEventListener('click', selectimg);
        img3.addEventListener('click', selectimg);
        img4.addEventListener('click', selectimg);
        img5.addEventListener('click', selectimg);
        img6.addEventListener('click', selectimg);
        function selectimg(e){
            e.preventDefault();
            const elem = e.target;
            const elemId = elem.getAttribute('id');
            const koi = document.getElementById('koi');
            const mai = document.getElementById('mai');
            const eni = document.getElementById('eni');
            const hii = document.getElementById('hii');
            const soi = document.getElementById('soi');
            const sci = document.getElementById('sci');

            if(elemId == 'img1'){
                koi.classList.remove('visible');
                mai.classList.remove('visible');
                eni.classList.remove('visible');
                hii.classList.remove('visible');
                soi.classList.remove('visible');
                sci.classList.remove('visible');
                img1.classList.remove('grayc');
                img2.classList.remove('grayc');
                img3.classList.remove('grayc');
                img4.classList.remove('grayc');
                img5.classList.remove('grayc');
                img6.classList.remove('grayc');
            }else if(elemId == 'img2'){
                koi.classList.add('visible');
                mai.classList.add('visible');
                eni.classList.remove('visible');
                hii.classList.remove('visible');
                soi.classList.remove('visible');
                sci.classList.remove('visible');
                img1.classList.add('grayc');
                img2.classList.add('grayc');
                img3.classList.remove('grayc');
                img4.classList.remove('grayc');
                img5.classList.remove('grayc');
                img6.classList.remove('grayc');
            }else if(elemId == 'img3'){
                koi.classList.add('visible');
                mai.classList.remove('visible');
                eni.classList.add('visible');
                hii.classList.remove('visible');
                soi.classList.remove('visible');
                sci.classList.remove('visible');
                img1.classList.add('grayc');
                img2.classList.remove('grayc');
                img3.classList.add('grayc');
                img4.classList.remove('grayc');
                img5.classList.remove('grayc');
                img6.classList.remove('grayc');
            }else if(elemId == 'img4'){
                koi.classList.add('visible');
                mai.classList.remove('visible');
                eni.classList.remove('visible');
                hii.classList.add('visible');
                soi.classList.remove('visible');
                sci.classList.remove('visible');
                img1.classList.add('grayc');
                img2.classList.remove('grayc');
                img3.classList.remove('grayc');
                img4.classList.add('grayc');
                img5.classList.remove('grayc');
                img6.classList.remove('grayc');
            }else if(elemId == 'img5'){
                koi.classList.add('visible');
                mai.classList.remove('visible');
                eni.classList.remove('visible');
                hii.classList.remove('visible');
                soi.classList.add('visible');
                sci.classList.remove('visible');
                img1.classList.add('grayc');
                img2.classList.remove('grayc');
                img3.classList.remove('grayc');
                img4.classList.remove('grayc');
                img5.classList.add('grayc');
                img6.classList.remove('grayc');
            }else if(elemId == 'img6'){
                koi.classList.add('visible');
                mai.classList.remove('visible');
                eni.classList.remove('visible');
                hii.classList.remove('visible');
                soi.classList.remove('visible');
                sci.classList.add('visible');
                img1.classList.add('grayc');
                img2.classList.remove('grayc');
                img3.classList.remove('grayc');
                img4.classList.remove('grayc');
                img5.classList.remove('grayc');
                img6.classList.add('grayc');
            }
        }
}