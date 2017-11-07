$(function() {
	/* 引入左侧导航栏 */
	$.get('/static/pages/adminMenu.html', function(data){
		$('#adminMenu').html(data);
	});

	/* 切换折叠指示图标 */
	$(".panel-heading").on('click', function(e) {
	    $(this).find("span").toggleClass("glyphicon-chevron-down");
	    $(this).find("span").toggleClass("glyphicon-chevron-up");
	});

	/* 调用接口：获取所有设备列表 */
	$.ajax({
	    url: '/admin/dev/list',
	    type: 'GET',
	    data: {},
	    dataType: 'JSON',
	    beforeSend: function(xhr) {
	        
	    }
	})
	.done(function(res) {
	    res = typeof(res) === 'string' ? JSON.parse(res) : res;
	    /* 展示设备列表 */
	    if (res.status == 200 && res.data.length) {
	    	var html = '';
	    	res.data.forEach(function(device, index) {
	    		html += '<tr>';
	    		html += '<td>' + device.id + '</td>';
	    		html += '<td>' + device.name + '</td>';
	    		html += '<td>' + device.devtype + '</td>';
	    		html += '<td>' + device.asset_number + '</td>';
	    		html += '<td>' + device.owner + '</td>';
	    		html += '<td>' + device.being_user + '</td>';
	    		html += '<td>' + device.ip + '</td>';
	    		html += '<td>' + device.console_info + '</td>';
	    		html += '<td>' + (device.if_online === 'y' ? '是' : '否') + '</td>';
	    		html += '<td>' + device.note + '</td>';
	    		html += '<td><button type="button" class="btn btn-primary btn-sm table-opt-btn">编&nbsp;辑</button><button type="button" class="btn btn-danger btn-sm">删&nbsp;除</button></td>';
	    		html += '</tr>';
	    	});
	    	$('#allDeviceList').append(html);
	    }
	})
	.fail(function(jqXHR, textStatus, errorThrown) {
	    console.log(errorThrown);
	})
	.always(function() {

	});
});
