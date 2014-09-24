$("#id_apartment").change(function(){
    var value=$(this).children('option:selected').val();
    if(value)
    {
        Dajaxice.home.getCollege(getCollegeCallBack,{"apartment":value});
    }
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
