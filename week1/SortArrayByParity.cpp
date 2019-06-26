class Solution {
public:
	vector<int> sortArrayByParity(vector<int>& A) {

		//initialize new array
		vector<int> result;

		for (int i : A) {
			if A[i] % 2 == 0
				result.insert(0,A[i]);
			else
				result.push_back(A[i]);
		}

		return result;
	}
};
