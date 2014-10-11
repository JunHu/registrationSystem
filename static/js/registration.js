$(document).ready(function(){
function getCollege()
{
    var value=$("#id_apartment").children('option:selected').val();
    if(value)
    {
        Dajaxice.home.getCollege(getCollegeCallBack,{"apartment":value});
    }
    else
    {
        $("#id_college").empty();
        $("<option value selected='selected'>---------</option>").appendTo("#id_college");
    }
}


getCollege();
$("#id_apartment").change(function(){
    getCollege();
});
function getCollegeCallBack(data)
{
    var college=data.college;
    $("#id_college").empty();
    $("<option value selected='selected'>---------</option>").appendTo("#id_college");
    for(var v in college)
    {
        $("<option value="+college[v][0]+">"+college[v][1]+"</option>").appendTo("#id_college");
    }
}


});

$("input[name='commit']").click(function(){
    if(confirm("相同学号只能提交一次, 确认是否提交报名信息...")){
        return true;
    }
    return false;
});
