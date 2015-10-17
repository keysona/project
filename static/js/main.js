		               
    $(function(){
    $("#a").val('');
    $("label").remove();
    $("#form_id").submit(function(){
    $(".item").remove();
    $("#resultscript").html('');
    $("#find").remove();
    $("#imgdiv").prepend("<h3 id='find'>Find pirture</h3>");
    var data = new FormData($('#form_id').get(0));
                $.ajax({
                    type:"POST",
                    url: "/file/upload/",
                    data : data,
                    cache: false,
                    contentType: false,
                    processData: false,
		    beforeSend:function(){
		         $.blockUI({ 
			 message: '<div>正在查询...请稍候</div>', 
			 css: { 
			 border: 'none', 
			 padding: '15px', 
			 backgroundColor: '#000', 
			 'font-size':'25px',
			 'border-radius':'25px',
			 '-webkit-border-radius': '25px', 
			 '-moz-border-radius': '25px', 
			 opacity: .5, 
			 color: '#fff' 
			 } });
		    },
                    success: function(data){
		        $.unblockUI
                        var tempdiv='';
			var tempscript='';
			$.each(data,function(index,content){
				    var width = content["width"];
				    var height = parseInt(content["height"]);
				    tempdiv += '<div class="'+'imgbox" style="width:'+width+'px;height:'+height+'px">'+"<div id = '"+content["name"] +"' class='item image'"+' onclick="'+"window.open('"+content["url"]+"')"+'" style="cursor:pointer;width:'+content["width"]+'px;height:'+content["height"]+'px'+'"></div><div class="'+'text"><div class="'+'imgtext" style="width:'+width+'px"><span>&nbsp;&nbsp;'+content["width"]+'X'+content["height"]+'&nbsp;&nbsp;</span><span>&nbsp;&nabsp;'+content["type"]+'&nbsp;&nbsp;</span><span>&nbsp;&nbsp;'+content["time"]+'&nbsp;&nbsp;</span></div></div></div>';
			    tempscript += "document.getElementById('"+content["name"]+"').innerHTML = ReferrerKiller.imageHtml('"+content["url"]+"');";
			});
                        $("#resultcontainer").html(tempdiv);
		        $("#resultcontainer").prepend("<h3 id='theresult'>The results</h3>");
			    
			    $("center").nextAll().remove();
			   // tempscript = tempscript + '$(".imgtext").hide();$(".imgbox").hover(function(){$(".imgtext",this).stop(true,false).sildeToggle(500);';
			    $("body").append($("<script />", {
			      html: tempscript
			      }));
			    $("body").append($("<script />",{
			    html:'$("imgtext").hide;$(".imgbox").hover(function(){$(".imgtext",this).stop(true,false).slideToggle(500)});'
			    }));
                    },
                    failure: function(){
                        $(this).addClass("error");
                    }
                });
                return false;
    });
    $(":file").change(function(){
	var file = this.files[0];
        var name = file.name;
        var size = file.size;
    	var type = file.type;
        $("#a").val(name);
        if(size > 10000){
            $("#form_id").trigger("submit");
        }
    });

});
