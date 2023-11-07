// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract ScholarshipManagement {
    address private owner;
    uint public scholarshipBudget;
    uint public minimumScore;

    mapping(address => uint) public scholarshipBalances;
    mapping(address => uint) public academicScores;
    mapping(address => uint[]) public academicTranscripts;

    event ScholarshipFunded(address indexed Donor, uint amount);
    event ScholarshipAwarded(address indexed student, uint amount);

    constructor(uint _budget, uint _minScore) {
        owner = msg.sender;
        scholarshipBudget = _budget;
        minimumScore = _minScore;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    receive() external payable {
        fundScholarship(); // Automatically fund the scholarship when receiving Ether.
    }

    fallback() external payable {
        fundScholarship(); // Automatically fund the scholarship when receiving Ether without data.
    }

    function addAcademicRecord(uint[] memory scores) external{
        require(scores.length == 3, "Transcript must contain scores for three subjects.");
        academicScores[msg.sender] = calculateAverageScore(scores);
        academicTranscripts[msg.sender] = scores;
    }

    function fundScholarship() public payable {
        require(msg.value > 0, "Amount must be greater than zero.");
        scholarshipBudget += msg.value;
        emit ScholarshipFunded(msg.sender, msg.value);
    }

    function awardScholarship(address student) public onlyOwner {
        require(academicScores[student] >= minimumScore, "Student does not meet minimum academic requirements.");
        uint scholarshipAmount = calculateScholarshipAmount(student);
        require(scholarshipBudget >= scholarshipAmount, "Insufficient scholarship budget.");
        scholarshipBudget -= scholarshipAmount;
        scholarshipBalances[student] += scholarshipAmount;
        emit ScholarshipAwarded(student, scholarshipAmount);
    }

    function withdrawScholarshipFunds() public  {
        uint balance = scholarshipBalances[msg.sender];
        require(balance > 0, "No scholarship funds available.");
        scholarshipBalances[msg.sender] = 0;
        payable(msg.sender).transfer(balance);
    }

    function calculateScholarshipAmount(address student) public view returns (uint) {
        uint score = academicScores[student];
        if (score >= minimumScore && score < 70) {
            return scholarshipBudget / 10;  // 10% of the budget for students with scores between minScore and 70
        } else if (score >= 70 && score < 85) {
            return scholarshipBudget / 5;  // 20% of the budget for students with scores between 70 and 85
        } else if (score >= 85) {
            return scholarshipBudget / 2;  // 50% of the budget for students with scores greater than or equal to 85
        } else {
            return 0;
        }
    }

    function calculateAverageScore(uint[] memory scores) internal pure returns (uint) {
        require(scores.length == 3, "Transcript must contain scores for three subjects.");
        uint totalScore = 0;
        for (uint i = 0; i < scores.length; i++) {
            require(scores[i] >= 0 && scores[i] <= 100, "Scores should be between 0 and 100.");
            totalScore += scores[i];
        }
        return totalScore / 3;
    }
}
