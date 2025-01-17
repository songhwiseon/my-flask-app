$(document).ready(function() {

    $("#user-address").on('click',function(){
        new daum.Postcode({
            oncomplete: function(data) {
            
                $("#user-address").val(data.address);
            
            }
        }).open();
    }); 

    $('#save-btn').click(function(){
        var id = $('#user-id').val();
        var pw = $('#user-pw').val();
        var nick = $('#user-nick').val();
        var address = $('#user-address').val();
        var type = $('#type-slt').val();
        var pwCheck = $('#user-pw-check').val();

        if(id == '' || pw == '' || nick == '' || address == '' || type == ''){
            alert('모든 필드를 입력해주세요.');
            return;
        }
        
        if(pw != pwCheck){
            alert('비밀번호가 일치하지 않습니다.');
            return;
        }

        
        $.ajax({
            url:'./api/user/add-user',
            type:'post',
        
            contentType:'application/json',
            data:JSON.stringify({
                id:id,
                pw:pw,
                nick:nick,
                address:address,
                type:type
            }),
            success:function(response){
                if(response.message == 'ok'){
                    alert('회원가입 완료');
                }else{
                    alert('회원가입 실패');
                }
            },
            error:function(error){
                console.error(error);
            }
            
        });
            
        
    }); 
});
