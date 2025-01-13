o
    {g�6  �                   @   s(  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZ	d dl
mZ d dlmZmZmZmZmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZmZ d d	lmZ d d
lmZ d dlm Z  d dl!m"Z" d dlm#Z#m$Z$ d dl%m&Z& edeeed�Z'e�(� Z)e)j*ddd�dd� �Z+dd� Z,e'�-e�.dg��dedefdd��Z/e'�-e�.d��dd� �Z0e'�-e�.dg��dedefd d��Z/d!d"� Z1e2d#k�re3d$� d%d&� Z4d'd(� Z5e�6� Z7z*ze7�8e4� � e7�8e5� � e7�9�  W n	 e:y�   Y nw W e7�;�  dS W e7�;�  dS e7�;�  w dS ))�    N)�progress_bar)�API_ID�API_HASH�	BOT_TOKEN�WEBHOOK�PORT)�ClientSession)�listen)�getstatusoutput)�web)�Client�filters)�Message)�	FloodWait)�StickerEmojiInvalid)�message)�InlineKeyboardButton�InlineKeyboardMarkup)�Ashu�bot)�api_id�api_hash�	bot_token�/T)�
allow_headc                 �   s   �t �d�S )Nz$https://github.com/AshutoshGoswami24)r   �json_response)�request� r   �m2.py�root_route_handler!   s   �
r   c                  �   s   �t jdd�} | �t� | S )Ni���)�client_max_size)r   �Application�
add_routes�routes)�web_appr   r   r   �
web_server&   s   �
r%   �start�mc                 �   s8   �|j tjttddd�gtddd�gg�d�I d H  d S )Nu5   ✜ ᴀsʜᴜᴛᴏsʜ ɢᴏsᴡᴀᴍɪ 𝟸𝟺 ✜zhttps://t.me/AshutoshGoswami24)�urlu+   🦋 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🦋zhttps://t.me/AshuSupport)�reply_markup)�
reply_textr   �
START_TEXTr   r   )r   r'   r   r   r   �account_login,   s   ������r,   �stopc                 �   s2   �|� dd�I d H  tjtjtjgtj�R �  d S )Nu$   ♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐭 ♦T)r*   �os�execl�sys�
executable�argv)�_r'   r   r   r   �restart_handler=   s   �r4   �uploadc           1      �   s	  �|� d�I d H }| �|jj�I d H }|�� I d H }|�d�I d H  d|jj� �}z5t|d��}|�� }W d   � n1 s>w   Y  |�d�}g }|D ]}	|�	|	�dd�� qLt
�|� W n   |� d�I d H  t
�|� Y d S |�d	t|�� d
��I d H  | �|jj�I d H }
|
j}|
�d�I d H  |�d�I d H  | �|jj�I d H }|j}|�d�I d H  |�tj�I d H  | �|jj�I d H }|j}|�d�I d H  z.|dkr�d}n%|dkr�d}n|dkr�d}n|dkr�d}n|dkr�d}n	|dkr�d}nd}W n t�y
   d}Y nw |�tj�I d H  | �|jj�I d H }|j}|�d�I d H  d}|dk�r3|}n|}|�tj�I d H  | �|jj�I d H  }}|j}|�d�I d H  |�� I d H  |j}|�d��sk|�d��rvtd|� d�� d}n|d k t|�dk�r�d}nt|�}�z�t|d t|��D �]�}	||	 d �d!d"��d#d$��d%d&��d'd&�}d| }d(|v �rt� 4 I d H �L}|j|d)d*d+d,d+d-d.d/d0d1d2d3d4d5d6�d7�4 I d H �}|�� I d H }t�d8|��d�}W d   �I d H  n1 I d H �s�w   Y  W d   �I d H  n1 I d H �sw   Y  nod9|v �r+tjd:|� �d;d<id7��� d= }nYd>|v �s?d?|v �s?d9|v �s?d@|v �r_dAd<dBdCdDdEdFdGdH�}d=|� ff} tjdI|| dJ�}!|!�� d= }n%dK|v �rr|�dL�dM }"dN|" dO }ndP|v �r�|�dL�dM }"dQ|" dR }||	 dS �dTd&��dUd&��dLd&��dVd&��dWd&��dXd&��dYd&��dZd&��d[d&��d\d&��d]d&�� � }#t!|��"d^�� d_|#d d`� � �}$da|v �r�db|� dc|� dd�}%n	db|� de|� df�}%dg|v �r�dh|$� di|� dj|� dk�}&n1da|v �rdl|� dm|� dn|$� dk�}&ndo|v �rdp|%� dq|� dn|$� dk�}&n	 dp|%� dt|� dn|$� dk�}&�zd{t!|��"d^�� d||#� d}|� d~|� d{�	}'d{t!|��"d^�� d||#� d|� d~|� d{�	}(d�|v �r�z&t#�||$�I d H })| j$|jj|)|(d��I d H }*|d7 }t
�|)� t%�&d� W n� t'�y� }+ z|� t!|+��I d H  t%�&|+j(� W Y d }+~+W �q�d }+~+ww dw|v �r�z1dh|$� d�|� dk�}&|&� d��},t
�)|,� | j$|jj|$� dw�|(d��I d H }*|d7 }t
�|$� dw�� W nd t'�y� }+ z|� t!|+��I d H  t%�&|+j(� W Y d }+~+W �q�d }+~+ww d�|$� d�|� d�|� d��}-|� |-�I d H }.t#�*||&|$�I d H }/|/}0|.�d�I d H  t#�+| ||'|0||$|.�I d H  |d7 }t%�&d� W �q� t�yb }+ z|� d�t!|+�� d�|$� d�|� ��I d H  W Y d }+~+�q�d }+~+ww W n t�y }+ z|� |+�I d H  W Y d }+~+nd }+~+ww |� d��I d H  d S )�Nu(   sᴇɴᴅ ᴍᴇ .ᴛxᴛ ғɪʟᴇ  ⏍Tz./downloads/�r�
z://�   uG   ∝ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐢𝐥𝐞 𝐢𝐧𝐩𝐮𝐭.u8   ɪɴ ᴛxᴛ ғɪʟᴇ ᴛɪᴛʟᴇ ʟɪɴᴋ 🔗** **uo   **

sᴇɴᴅ ғʀᴏᴍ  ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛᴀʟ ɪs 1uz   ∝ 𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞�144�256x144�240�426x240�360�640x360�480�854x480�720�1280x720�1080�	1920x1080�UNu   ️ ⁪⁬⁮⁮⁮�Robinzhttp://zhttps://zwget 'z' -O 'thumb.jpg'z	thumb.jpg�nozfile/d/zuc?export=download&id=zwww.youtube-nocookie.com/embedzyoutu.bez?modestbranding=1� z/view?usp=sharing�	visioniasz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zen-US,en;q=0.9zno-cachez
keep-alivezhttp://www.visionias.in/�iframe�navigatez
cross-site�1zuMozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36z("Chromium";v="107", "Not=A?Brand";v="24"z?1z	"Android")�AcceptzAccept-LanguagezCache-Control�
Connection�Pragma�RefererzSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-SitezUpgrade-Insecure-Requestsz
User-Agentz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platform)�headersz(https://.*?playlist.m3u8.*?)\"zvideos.classplusappzChttps://api.classplusapp.com/cams/uploader/video/jw-signed-url?url=�x-access-token�\eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r(   ztencdn.classplusappz media-cdn-alisg.classplusapp.comzmedia-cdn.classplusappzapi.classplusapp.comzMobile-Androidz1.4.37.1�18�5d0d17ac8b3c9f51z(2848b866799971ca_2848b8667a33216c_SDK-30�gzip)�HostrR   z
user-agentzapp-versionzapi-versionz	device-idzdevice-detailszaccept-encodingz>https://api.classplusapp.com/cams/uploader/video/jw-signed-url)rQ   �paramsz/utkarshapp.mpdr   �����z$https://apps-s3-prod.utkarshapp.com/z/utkarshapp.comz/master.mpdz&https://d26g5bnklkwsh4.cloudfront.net/z/master.m3u8r   �	�:�+�#�|�@�*�.�https�http�   z) �<   �youtuz
b[height<=z][ext=mp4]/bv[height<=z!][ext=mp4]+ba[ext=m4a]/b[ext=mp4]z]/bv[height<=z]+ba/b/bv+ba�acecwplyzyt-dlp -o "z" -f "bestvideo[height<=zQ]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "�"z yt-dlp -i -f "bestvideo[height<=z=]+bestaudio" --no-keep-video --remux-video mkv --no-warning "z" -o "zplayer.vimeozyt-dlp -f "z/+bestaudio" --no-keep-video --remux-video mkv "�m3u8�
livestreamz%" --no-keep-video --remux-video mkv "�0�unknownz.pdf�download�pdfzC+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "z**z. u   .mkv

Batch Name  » u   

Downloaded By » u   .pdf

Batch Name  » �drive)�chat_id�document�captionz.pdf" "z -R 25 --fragment-retries 25uZ   **❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »

📝 𝐍𝐚𝐦𝐞 » u!   
⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » u   

🔗 𝐔𝐑𝐋 »** `�`uZ   ⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝
u   
⌘ 𝐍𝐚𝐦𝐞 » u   
⌘ 𝐋𝐢𝐧𝐤 » uE   ✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐨𝐧𝐞),r*   r	   �chat�idrm   �delete�open�read�split�appendr.   �remove�edit�len�textr   �Q1_TEXT�	Exception�C1_TEXT�T1_TEXT�
startswithr
   �int�range�replacer   �get�re�search�group�requests�json�strip�str�zfill�helper�send_document�time�sleepr   �x�system�download_video�send_vid)1r   r'   �editable�inputr�   �path�f�content�links�i�input0�raw_text�input1�	raw_text0�input2�	raw_text2�res�input3�	raw_text3�highlighter�MR�input6r   �	raw_text6�thumb�count�Vr(   �session�respr~   rQ   rX   �responseru   �name1�name�ytf�cmd�cc�cc1�ka�copy�e�download_cmd�Show�prog�res_file�filenamer   r   r   r,   C   s�  �
�


���

�
���,�*��
���



�
�


� 



((

�
��


���
�
��� �� #��c                  �   s\   �t r,t� I d H } t�| �}|�� I d H  t�|dt�}|�� I d H  tdt� �� d S d S )Nz0.0.0.0zWeb server started on port )	r   r%   r   �	AppRunner�setup�TCPSiter   r&   �print)�app�runner�siter   r   r   �main@  s   �
�r�   �__main__u�  
    █░█░█ █▀█ █▀█ █▀▄ █▀▀ █▀█ ▄▀█ █▀▀ ▀█▀     ▄▀█ █▀ █░█ █░█ ▀█▀ █▀█ █▀ █░█   
    ▀▄▀▄▀ █▄█ █▄█ █▄▀ █▄▄ █▀▄ █▀█ █▀░ ░█░     █▀█ ▄█ █▀█ █▄█ ░█░ █▄█ ▄█ █▀█ c                   �   s   �t �� I d H  d S �N)r   r&   r   r   r   r   �	start_botS  s   �r�   c                   �   s   �t � I d H  d S r�   )r�   r   r   r   r   �	start_webV  s   �r�   )<r.   r�   r0   r�   r�   �asyncior�   �
subprocess�corer�   �utilsr   �varsr   r   r   r   r   �aiohttpr   �pyromodr	   r
   r   �pyrogramr   r   �pyrogram.typesr   �pyrogram.errorsr   �*pyrogram.errors.exceptions.bad_request_400r   �!pyrogram.types.messages_and_mediar   r   r   �styler   r   �RouteTableDefr#   r�   r   r%   �
on_message�commandr,   r4   r�   �__name__r�   r�   r�   �get_event_loop�loop�create_task�run_forever�KeyboardInterruptr-   r   r   r   r   �<module>   sl    

 }
�����