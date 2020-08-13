let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

const generateTarget = () => {
    return Math.floor(Math.random() * 10);
}

const getAbsoluteDifference = (num1, num2) => {
    return Math.abs(num1 - num2);
}

const compareGuesses = (humanGuess, computerGuess, target) => {
    const humanDiff = getAbsoluteDifference(humanGuess, target);
    const computerDiff = getAbsoluteDifference(computerGuess, target);
    
    if (humanDiff <= computerDiff) {
        return true;
    } else {
        return false;
    }
}

const updateScore = winner => {
    if (winner === "human") {
        humanScore++;
    } else if (winner === "computer") {
        computerScore++;
    }
}

const advanceRound = () => {
    currentRoundNumber++;
}
