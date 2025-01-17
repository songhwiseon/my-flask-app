$(document).ready(function () {

    function message(label, confidence){
        if (label == 'Pneumonia' && confidence > 0.8){
            return '매우 위험 : 치료 필요';
        }else if(label == 'Pneumonia' && confidence > 0.5){
            return '위험 : 병원 방문 필요';
        }else if(label == 'Pneumonia' && confidence > 0.2){
            return '주의 : 관리 필요';
        }else{
            return '정상';
        }

    }



    
    function Korean(label) {
        const labelMap = {
            'Normal': '정상',
            'Pneumonia': '폐렴'
        };
        return `${label} (${labelMap[label]})`;
    }


    $('#predict-btn').click(function(){
        var name = $('#name').val();
        var age = $('#age').val();
        var image = $('#imageInput')[0].files[0];

        console.log(name,age,image);   

        var post_data = {
            name:name,
            age:age,
            image:image
        }

        console.log(post_data); 

        $.ajax({
            url:'/api/ai/covid-19',
            type:'post',
            dataType:'json',
            contentType:'application/json',
            data:JSON.stringify(post_data),
        });


    });


    $('#uploadForm').on('submit', function (e) {
        e.preventDefault();
        
        // FormData 객체 생성
        const formData = new FormData();
        
        // 파일과 이름 가져오기
        const imageFile = $('#imageInput')[0].files[0];
        const name = $('#name').val();
        const age = $('#age').val();


        // 유효성 검사
        if (!imageFile) {
            alert("이미지 파일을 선택해주세요.");
            return;
        }

        if (!name) {
            alert("이름을 입력해주세요.");
            return;
        }

        if (!age) {
            alert("나이를 입력해주세요.");
            return;
        }


        // FormData에 데이터 추가
        formData.append('image', imageFile);
        formData.append('name', name);
        formData.append('age', age);


        // AJAX 요청
        $.ajax({
            url: '/api/ai/covid-19',
            type: 'POST',
            data: formData,
            processData: false,  // 필수: FormData 처리 방지
            contentType: false,  // 필수: Content-Type 헤더 자동 설정
            
            success: function (response) {
                if (response.label) {
                    $('#result').html(`
                        <div class="result-box">
                            <p>${name}님의 검사 결과는 ${Korean(response.label)} 입니다.</p>
                            <p>${(response.confidence * 100).toFixed(2)}%의 확률로 ${Korean(response.label)} 입니다.</p>
                            <p>위험도 : ${message(response.label, response.confidence)}</p>
                        </div>
                    `);
                } else {
                    $('#result').text('예상치 못한 오류가 발생했습니다.');
                }
            },
            error: function (xhr) {
                const errorMsg = xhr.responseJSON?.error || '요청 처리 중 오류가 발생했습니다.';
                $('#result').text(`Error: ${errorMsg}`);
            }
        });
    });
});
