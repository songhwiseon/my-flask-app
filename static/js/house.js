$(document).ready(function() {

    $('#predict-btn').click(function(){
        var area = $('#area').val();
        var rooms = $('#rooms').val();
        var year_built = $('#year_built').val();
        var income = $('#income').val();
        var school_rating = $('#school-rating').val();
        var transit_score = $('#transit-score').val();

        var post_data = {
            area:area,
            rooms:rooms,
            year_built:year_built,
            income:income,
            school_rating:school_rating,
            transit_score:transit_score
        }

        console.log(post_data);

        $.ajax({
            url:'/api/ai/add-predict',
            type:'post',
            dataType:'json',
            contentType:'application/json',
            data:JSON.stringify(
                {
                    area:area,
                    rooms:rooms,
                    year_built:year_built,
                    income:income,
                    school_rating:school_rating,
                    transit_score:transit_score
                }   
            ),
            success:function(response){
                if(response.message == 'ok'){



                    $('#result-text-1').text(response.price_lin);
                    $('#result-text-2').text(response.price_rf);
                    alert('예측 완료');
       
            
            }},
            error:function(error){
                console.error(error);
            }


        }); 

       



            
        
    }); 
});


