
// global variable to keep the count of books rows added, initialized to 1 as one row exists by default in the index page
//var row=1;

// add a row dynamically to the unorderedlist using jquery
$("#plus").click(function(){
//console.log(row);
$("#myBooks").append('<li class="booksList" style="height: 40px"><div class="book container-fluid"><div style="float:left; margin-right: 5px;"> Select book type: <select id="bookType" name="bookType" class="bookType btn btn-primary "><option value="regular">Regular</option><option value="fiction">Fiction</option><option value="novel">Novel</option></select></div><div style="float:left; margin-left: 10px;">Enter quantity: <input type="number" id="booksQuantity" class="bookQuantity" name="booksQuantity" min="1" minlength="1" onkeypress="return (event.charCode !=8 && event.charCode ==0 || (event.charCode >= 48 && event.charCode <= 57))" /></div><div style="float:left; margin-left: 10px;">Enter duration(in days): <span class="glyphicon glyphicon-question-sign" data-toggle="tooltip" title="round the duration to the next nearest day i.e., duration should be 2 if the number of hours is >24 and <=48 hours"> </span><input type="number" id="dayDuration" class="dayDuration" name="dayDuration" min="1" minlength="1" onkeypress="return (event.charCode !=8 && event.charCode ==0 || (event.charCode >= 48 && event.charCode <= 57))" /></div><a href="javascript:void(0);" onclick="remove(this)"><span class="glyphicon glyphicon-trash"></span></a></div></li>')
});


// remove the selected particular row from the list
function remove(link){
    link.closest("li").remove()
}

// display tooltip over the duration field label
$('[data-toggle="tooltip"]').tooltip();


// function to build the JSON and send to the POST API over http endpoint
function mysubmit(){
    var books = [];
    var booksList = document.getElementsByClassName("booksList");
    for(var i=0; i<booksList.length; i++) {
        // constructing JSON object
        var thisBook = {};
        thisBook["bookType"] = booksList[i].getElementsByClassName("book")[0].getElementsByClassName("bookType")[0].value;
        thisBook["bookQuantity"] = Number(booksList[i].getElementsByClassName("book")[0].getElementsByClassName("bookQuantity")[0].value);
        thisBook["dayDuration"] = Number(booksList[i].getElementsByClassName("book")[0].getElementsByClassName("dayDuration")[0].value);
        if(thisBook["bookType"] == "" || thisBook["bookQuantity"] == "" || thisBook["dayDuration"] == ""){
        alert("all fields must be filled, please remove unecessary information.");
        return;
        }
        books.push(thisBook);
    }
    console.log(books);

    // calling POST APIs
    $.ajax({
    url: "http://127.0.0.1:5020/calculate",
    type: "POST",
    data: JSON.stringify(books),
    contentType: "application/json",
    success: function(result){
    console.log("success")
    console.log(result)
    window.location.href = result["url"]
    },
    error: function(error){
    console.log(`Error ${error}`)
    }
    })
}


