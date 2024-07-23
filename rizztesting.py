<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rizz Line Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-bottom: 20px;
        }
        p {
            font-size: 18px;
            max-width: 300px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Rizz Line Generator</h1>
    <button onclick="generateRizz()">Generate Rizz</button>
    <p id="result"></p>
    <button id="copyButton" onclick="copyToClipboard()" style="display: none;">Copy</button>

    <script>
        const pickupLines = [
            "Can I be your snowflake? I promise to never melt away from your heart",
            "Are you French? Because Eiffel for you",
            "Are you a Wi-Fi signal? Because I’m feeling a strong connection",
            "No pen, no paper...but, you still draw my attention",
            "Are you a heart? Because I'd never stop beating for you",
            "I believe in following my dreams, so you lead the way",
            "If being beautiful was a crime, you’d be on the most wanted list",
            "Kissing is a love language. Want to start a conversation with me?",
            "Are you iron? Because I don’t get enough of you",
            "Should we get coffee? Cause I like you a latte",
            "You should be Jasmine without the 'Jas'",
            "Are you a Disney ride? Because I'd wait forever for you",
            "Are you water? Because I'd die without you",
            "I see you like tequila. Does that mean you'll give me a shot?",
            "Hey, I’m sorry to bother you, but my phone must be broken because it doesn’t seem to have your number in it",
            "Are you a boxer? Because you're a total knockout",
            "Are you public speaking? Because you make me really nervous",
            "Are you good at math? Me neither, the only number I care about is yours",
            "I'm not a photographer, but I can picture us together",
            "Are you an exam? Because my mom told me not to cheat on important things",
            "Hi. I’m Mrs./Mr. Right. Someone said you were looking for me",
            "Einstein said that nothing is faster than the speed of light. But he never saw how fast I would fall for you",
            "When we met, it was like listening to a song for the first time that I knew would eventually become my favorite",
            "I see you’re a fan of vodka. Does that mean you’ll give me a shot?",
            "All the pickup lines are taken, but are you?",
            "I'm not a physicist, but I feel a strong magnetic attraction here. Is it just me?",
            "I'm no geologist, but I feel a seismic shift in my world whenever you’re near",
            "Is your name Google? Because you’ve got everything I’ve been searching for",
            "You must be a high test score because I want to take you home and show you to my mother",
            "Hey. I’m the one you’ve been looking for. You can delete this app now",
            "Numbers start with 1 2 3. The alphabet starts with A B C. But the universe starts with U N I",
            "You owe me a drink because I dropped mine when I saw you",
            "You must be an important line in a book because seeing you is a highlight",
            "Are you Nemo? Because I've been trying to find you",
            "Are you a bank loan? Because you have my interest",
            "I hope you know CPR, because you just took my breath away",
            "Are you the sun? Because I could stare at you all day, and it’d be worth the risk",
            "Are you a beaver? Because DAM!",
            "Are you a keyboard? Because you're just my type",
            "My mom said sharing is caring but, no...you're all mine!",
            "Are you John Cena? Because I've never Cena girl like you before",
            "It's time to pay up. It's the first of the month, and you've been living in my mind rent-free",
            "Are you a light? Because you always make me feel bright",
            "Just so you know, I'm a felon...because I felon love with you",
            "Do you like Star Wars? Cause Yoda only one for me",
            "Are you chicken fingers and fries? Because I don't care how many options I have, I will always choose you",
            "It's a good thing I have a library card because I've been checking you out",
            "Do you have a bandaid? My knees hurt from falling for you"
        ];

        function generateRizz() {
            const line = pickupLines[Math.floor(Math.random() * pickupLines.length)];
            const resultElement = document.getElementById('result');
            const copyButton = document.getElementById('copyButton');
            resultElement.textContent = line;
            copyButton.style.display = 'inline-block';
        }

        function copyToClipboard() {
            const resultElement = document.getElementById('result');
            navigator.clipboard.writeText(resultElement.textContent).then(function() {
                alert('Copied to clipboard');
            }, function() {
                alert('Failed to copy');
            });
        }
    </script>
</body>
</html>
