

//익명함수

//on(문자열, 함수) 함수
// $(document).ready(function(){

    
//     $("#my-btn").on('click',function(){
          
         
        // $("#my-txt").html($("#my-input").val()); //input값 가져오기
        // //코드 설명
        // //val() : input 값을 가져오는 함수
        // //html() : 태그 내용을 가져오는 함수    
//         var v = $("#my-input").val();
//         $("#my-txt").html(v);
//         $("#my-btn").css("background-color",v);



//     });
// });


$(document).on('click','.todo-box',function(){

    var todo_id = $(this).data("todo-id");

    location.href = "http://127.0.0.1:5000/td?todo-id="+todo_id;
});
      


function fetchTodo(){
    $.ajax({
        url : "https://jsonplaceholder.typicode.com/todos/",
        type : "GET",
        data : {},
        success : function(todos){
            console.log(todos);

            for(var i = 0; i < todos.length; i++){
                var todo = todos[i];
                $("#todo-list").append(`<tr style="cursor: pointer;" class="todo-box" data-todo-id="${todo.id}">
                    <td>${todo.id}</td>
                    <td>${todo.userId}</td>
                    <td>${todo.title}</td>
                    <td>${todo.completed}</td>
                </tr>`);
            }
        }
    });
      

}

$(document).ready(function(){

    fetchTodo();    

//jsonplaceholder 사이트에서 데이터 가져오기

    $.ajax({
        url : "https://jsonplaceholder.typicode.com/todos/1",
        type : "GET",
        data : {},
        success : function(todo){
            console.log(todo);
            $("#todo-id").text(todo.id);
            $("#user-id").text(todo.userId);
            $("#title").text(todo.title);
            $("#completed").text(todo.completed.toString());
        
        },
        error : function(error){
        
        }
    });



    




    var index = 0;
    
    //my-address 클릭시 주소 창을 띄우는 코드
    $("#my-address").on('click',function(){
        new daum.Postcode({
            oncomplete: function(data) {
            
                $("#my-address").val(data.address);
            
            }
        }).open();
    }); 


    $("#save-btn").on('click',function(){
        var name = $("#my-name").val();
        var age = $("#my-age").val();
        var address = $("#my-address").val();
    
    //  console.log(name,age,address);
    

        //유효성 검사

        if(name == "" || age == "" || address == ""){
            alert("모든 항목을 입력해주세요");
            return;
        }   
    
    

        index++;    

        $("#user-list").append(`<tr>
            <td>${index}</td>
            <td>${name}</td>
            <td>${age}</td>
            <td>${address}</td>
        </tr>`);
    
    });
})













