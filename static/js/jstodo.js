
$(document).ready(function(){
    var todo_id = $("#todo-id").val();
    //console.log(todo_id);

    $.ajax({
        url : "https://jsonplaceholder.typicode.com/todos/"+todo_id,
        type : "GET",
        success : function(todo){
            $("#todoid").text(todo.id);
            $("#user-id").text(todo.userId);
            $("#title").text(todo.title);
            $("#completed").text(todo.completed);       
        },

        error : function(error){
            console.log(error);
        }   
    });


    $.ajax({
        url : "http://127.0.0.1:5000/test",
        type : "POST",
        data : {id : "1", pw : "1234"},
        success : function(data){
            if(data == "ok"){
                alert("ok");
            }else{
                alert("no");
            }
        }
    });
                           

});




