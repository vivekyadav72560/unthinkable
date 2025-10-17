document.addEventListener('DOMContentLoaded', () => {
    const getRecsBtn = document.getElementById('get-recs-btn');
    const userIdInput = document.getElementById('user-id');
    const recommendationsContainer = document.getElementById('recommendations-container');
    const loadingIndicator = document.getElementById('loading');

    const fetchRecommendations = async (userId) => {
        if (!userId) {
            alert('Please enter a User ID.');
            return;
        }

        loadingIndicator.classList.remove('hidden');
        recommendationsContainer.innerHTML = '';

        try {
            // NOTE: Ensure your Flask backend is running on http://127.0.0.1:5000
            const response = await fetch(`http://127.0.0.1:5000/recommendations?user_id=${userId}`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            displayRecommendations(data.recommendations);

        } catch (error) {
            console.error('Failed to fetch recommendations:', error);
            recommendationsContainer.innerHTML = `<p style="color: red;">Error: Could not fetch recommendations. Make sure the backend server is running.</p>`;
        } finally {
            loadingIndicator.classList.add('hidden');
        }
    };

    const displayRecommendations = (recs) => {
        if (!recs || recs.length === 0) {
            recommendationsContainer.innerHTML = '<p>No recommendations available for this user.</p>';
            return;
        }

        recs.forEach(rec => {
            const product = rec.product;
            const explanation = rec.explanation;

            const card = document.createElement('div');
            card.className = 'product-card';
            card.innerHTML = `
                <h3>${product.name}</h3>
                <span class="category">${product.category}</span>
                <p class="description">${product.description}</p>
                <div class="explanation">
                    <p><strong>Why you might like this:</strong> ${explanation}</p>
                </div>
            `;
            recommendationsContainer.appendChild(card);
        });
    };

    getRecsBtn.addEventListener('click', () => {
        fetchRecommendations(userIdInput.value);
    });
    
    // Fetch initial recommendations for User 1 on page load
    fetchRecommendations(1);
});