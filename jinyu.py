
const Discord = require('discord.js');
var request = require('request');
var cheerio = require('cheerio');
var bot = new Discord.Client();

var bool = 0;
var sw = false;
var fanhao = ["HNDS-045",
              "MIAD-908",
              "FCMQ-019",
              "ID-046",
              "AVOP-279",
              "STAR-647",
              "200GANA-894",
              "SDDE-465",
              "200GANA-1189",
              "EBOD-590",
              "GDHH-076",
              "TYOD-365"];
var remind = {
    author:"none",
    hr:0,
    mn:0,
    str:"nothing"
};

var prefix = "!";
var bigWord = ['𝓐','𝓑','𝓒','𝓓','𝓔','𝓕','𝓖','𝓗','𝓘','𝓙','𝓚','𝓛','𝓜','𝓝','𝓞','𝓟','𝓠','𝓡','𝓢','𝓣','𝓤','𝓥','𝓦','𝓧','𝓨','𝓩'];
var smallWord = ['𝓪','𝓫','𝓬','𝓭','𝓮','𝓯','𝓰','𝓱','𝓲','𝓳','𝓴','𝓵','𝓶','𝓷','𝓸','𝓹','𝓺','𝓻','𝓼','𝓽','𝓾','𝓿','𝔀','𝔁','𝔂','𝔃'];

//Bot執行成功提示
bot.on('ready', () => {
    console.log(`Logged in as ${bot.user.username}!`);
});

bot.on('message', (message) => {

    if(message.content.startsWith(prefix + "靜音") && message.member.roles.find("name", "均諭")){
        let member = message.mentions.members.first();
        member.setMute(true, '原因');
        message.channel.sendMessage(member + "已經被靜音");
        //member.setNickname('晴玥的化身', '原因');
        console.log(`muted`);
    }
    
    if(message.content.startsWith(prefix + "靜音") && message.member.roles.find("name", "均諭左右手")){
        let member = message.mentions.members.first();
        member.setMute(true, '原因');
        message.channel.sendMessage(member + "已經被靜音");
        //member.setNickname('晴玥的化身', '原因');
        console.log(`muted`);
    }
    if(message.content.startsWith(prefix + "靜音") && message.member.roles.find("name", "貴族")){
        let member = message.mentions.members.first();
        member.setMute(true, '原因');
        message.channel.sendMessage(member + "已經被靜音");
        //member.setNickname('晴玥的化身', '原因');
        console.log(`muted`);
    }
    if(message.content.startsWith(prefix + "講話") && message.member.roles.find("name", "貴族")){
        let member = message.mentions.members.first();
        member.setMute(false, '原因');
        message.channel.sendMessage(member + "已經可以講話了");
        //member.setNickname('晴玥的化身', '原因');
        console.log(`muted`);
    }
    if (message.author === bot.user) return;
    if(message.content.startsWith(prefix + "轉換")){
        var str = message.content.substring(4);
        var str2 = "";
        for (var i=0;i<str.length;i++){
            if(str.charAt(i) >= 'A' && str.charAt(i) <= 'Z'){
                str2 += bigWord[str.charAt(i).charCodeAt()-65];
            }
            else if(str.charAt(i) >= 'a' && str.charAt(i) <= 'z'){
                str2 += smallWord[str.charAt(i).charCodeAt()-97];
            }
            else{
                str2 += str.charAt(i);
            }
        }
        message.channel.sendMessage(str2);
    }
    if (message.content.startsWith(prefix + "番號")){
        var rnd = Math.floor(Math.random()*fanhao.length);
        console.log(rnd);
        message.reply('均諭喜歡這部 '+ fanhao[rnd] + ' 推薦你去看看哦:relaxed: ');
    }
    if(message.content.startsWith(prefix + "均諭幾點了")){
        message.reply('現在' + new Date().getHours() + '點' + new Date().getMinutes() + '分哦');
    }
    if(message.content.startsWith(prefix + "均諭提醒我")){
        remind.author = message.author;
        remind.hr = message.content.substring(7,9);
        remind.mn = message.content.substring(10,12);
        remind.str = message.content.substring(13);
        console.log(remind.author);
        console.log(remind.hr);
        console.log(remind.mn);
        console.log(remind.str);

    }
    if(new Date().getHours() == remind.hr && new Date().getMinutes() == remind.mn){
        message.channel.sendMessage(remind.author + "," + remind.str + "囉");
        remind.hr = -1;
    }
    if(message.content.startsWith(prefix + "戰績網")) {
        record(message.content.substring(4));

    }
    if (message.content === '均諭說話') {
        message.reply('我要調皮囉 :smile: :smile: ');
        sw = true;
        // message.channel.sendMessage(message.content);
    }

    else if (message.content === '均諭閉嘴'){
        message.reply('好 我閉嘴 :speak_no_evil:');
        sw = false;
    }
    if (sw){
        message.channel.sendMessage(message.content);
    }

    function record(name){
        var request = require("request");
        var cheerio = require("cheerio");

        var url = "https://lol.moa.tw/summoner/show/"+name;

        // 取得網頁資料
        request(url, function (error, response, body) {
          if (!error) {

            // 用 cheerio 解析 html 資料
            var $ = cheerio.load(body);

            // 篩選有興趣的資料
            var temperature = $("[data-variable='temperature'] .wx-value").html();
            var humidity = $("[data-variable='humidity'] .wx-value").html();
            var rank = $("div.col-xs-6").text();
            // 輸出
            // console.log("rank"+rank);
            message.channel.sendMessage(rank);
          } else {
            console.log("擷取錯誤：" + error);
          }
        });
    }

    //GPU查詢功能
    if (message.content.startsWith(prefix + "gpu")) {
        var searchGPU = message.content.substring(5).split('\n')[0];
        console.log(searchGPU);
        message.channel.sendMessage("等我一下 我找找");
        var url = 'https://www.futuremark.com/hardware/gpu';
        request(url, function (err, res, body) {
            // 跟futurerank要資料
            var $ = cheerio.load(body);
            // 把要到的資料放進 cheerio
            var gpuList = []

            $('a.productnameBold').each(function (i, elem) {
                //parent()回到上層html-tag children()到下層html-tag
                gpuList.push($(this).text() + "-" +
                    $(this).parent().parent().children().children('.barHolder').children('.bar').text()
                );
            });
            var output = [];
            //整理從cheerio取得的資料 存放至output[]
            for (var i = 0; i < gpuList.length; i++) {
                output.push({
                    gpu: gpuList[i].split("-")[0],
                    score: gpuList[i].substring(gpuList[i].indexOf("- ") + 2).split(" ")[0]
                });
            }
            for (var i = 0; i < output.length; i++) {

                var gpu = output[i].gpu;
                var compareGPU = gpu;
                var score = output[i].score;
                //console.log(searchGPU.toString().toLowerCase());
                //console.log(output[i].gpu.toString().toLowerCase());
                if (searchGPU.toString().toLowerCase() === output[i].gpu.toString().toLowerCase()) {
                    if(score>11750){
                        var diff = score - 11750;
                        message.channel.sendMessage(score);
                        message.channel.sendMessage("你的顯卡 " + gpu + " 比建鈞的RX470高 " + diff + " 分喔");
                    }
                    else if(score<11750){
                        var diff = 11750 - score;
                        message.channel.sendMessage(score);
                        message.channel.sendMessage("你的顯卡 " + gpu + " 比建鈞的RX470低 " + diff + " 分喔");
                    }
                    else{
                        message.channel.sendMessage(score);
                        message.channel.sendMessage("你打LOL是不是很卡030");
                    }
                    bool = 1;
                    break;
                }
            }
            if (bool) {
                bool = 0;
            }
            else {
                message.channel.sendMessage("沒有這張顯卡或是你打錯囉:)");
                message.channel.sendMessage("Ex:amd radeon rx 470 || nvidia geforce gtx 1080 ti");
            }
        });

    }
    //CPU查詢功能
    if (message.content.startsWith(prefix + "cpu")) {
        var searchCPU = message.content.substring(5).split('\n')[0];
        console.log(searchCPU);
        message.channel.sendMessage("等我一下 我找找");
        var url = 'https://www.futuremark.com/hardware/cpu';
        request(url, function (err, res, body) {
            // 跟futurerank要資料
            var $ = cheerio.load(body);
            // 把要到的資料放進 cheerio
            var cpuList = []

            $('a.productnameBold').each(function (i, elem) {
                //parent()回到上層html-tag children()到下層html-tag
                cpuList.push($(this).text() + "^" +
                    $(this).parent().parent().children().children('.barHolder').children('.bar').text()
                );
            });
            var output = [];
            //整理從cheerio取得的資料 存放至output[]
            for (var i = 0; i < cpuList.length; i++) {
                output.push({
                    cpu: cpuList[i].split("^")[0],
                    score: cpuList[i].substring(cpuList[i].indexOf("^ ") + 2).split(" ")[0]
                    
                });
                //message.channel.sendMessage(output);
            }
            for (var i = 0; i < output.length; i++) {

                var cpu = output[i].cpu;
                var compareCPU = cpu;
                var score = output[i].score;
                //console.log(searchCPU.toString().toLowerCase());
                //console.log(output[i].gpu.toString().toLowerCase());
                if (searchCPU.toString().toLowerCase() === output[i].cpu.toString().toLowerCase()) {
                    if(score>5620){
                        var diff = score - 5620;
                        message.channel.sendMessage(score);
                        message.channel.sendMessage("你的處理器 " + cpu + " 比建鈞的 i5-6400 高 " + diff + " 分喔");
                    }
                    else if(score<=5620){
                        var diff = 5620 - score;
                        message.channel.sendMessage(score);
                        message.channel.sendMessage("你的處理器 " + cpu + " 比建鈞的 i5-6400 低 " + diff + " 分喔");
                        
                    }
                    else{
                        message.channel.sendMessage(score);
                        message.channel.sendMessage("你打LOL是不是常常掉FPS");
                    }
                    bool = 1;
                    break;
                }
            }
            if (bool) {
                bool = 0;
            }
            else {
                message.channel.sendMessage("沒有這顆CPU或是你打錯囉:)");
                message.channel.sendMessage("Ex:amd ryzen 5 1600 || intel core i9-7980XE");
            }
        });

    }
    //組電腦查詢功能
    if (message.content.startsWith(prefix + "幫我組intel")) {
        var budge = message.content.substring(10).split('K')[0];
        if(budge<=5){
            message.channel.sendMessage("https://cdn-shop.adafruit.com/970x728/50-06.jpg");
        }
        else if(budge>=6 && budge<=15){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/i10K.png");

        }
        else if(budge>16 && budge<=25){
            cmessage.channel.sendMessage("http://reverie.000webhostapp.com/TEST/i120K.png");
            
        }
        else if(budge>26 && budge<=35){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/i30K.png");
                        
        }
        else if(budge>36 && budge<=45){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/i40K.png");
                        
        }
        else if(budge>46 && budge<=55){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/i50K.png");
                        
        }
        else if(budge>55) {
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/i60K.png");
                        
        }
        //console.log(budge);
    }

    if (message.content.startsWith(prefix + "幫我組AMD")) {
        var budge = message.content.substring(8).split('K')[0];
        if(budge<=6){
            message.channel.sendMessage("https://www.raspberrypi.org/app/themes/mind-control/images/home-products-cta__image.png");
        }
        else if(budge>=6 && budge<=15){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/a10K.png");

        }
        else if(budge>=16 && budge<=25){
            cmessage.channel.sendMessage("http://reverie.000webhostapp.com/TEST/a20K.png");
            
        }
        else if(budge>=26 && budge<=35){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/a30K.png");
                        
        }
        else if(budge>=36 && budge<=45){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/a40K.png");
                        
        }
        else if(budge>=46 && budge<=55){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/a50K.png");
                        
        }
        else if(budge>=56 && budge<=65){
            message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/a60K.png");
                        
        }
        else if(budge>65)
        message.channel.sendMessage("http://reverie.000webhostapp.com/TEST/a70K.png");
        //console.log(budge);
    }
});
bot.login('MzM0OTg5MDI5OTY1NTYxODU4.DSO7JA.QTYyhKJPoRFGsMJ-g4aPJFoyg1I');

