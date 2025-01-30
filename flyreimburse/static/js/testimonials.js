const testimonials = [
    {
        text: '"Shërbimi i FlyReimburse është i shkëlqyer. Ekipi më ndihmoi të merrja kompensimin tim shpejt dhe pa probleme!"',
        author: '- Klienti i Kënaqur'
    },
    {
        text: '"Falë FlyReimburse, unë mora kompensimin për fluturimin tim të vonuar brenda pak javësh!"',
        author: '- Anisa, Tiranë'
    },
    {
        text: '"Ekipi ishte shumë profesional dhe më ndihmoi në çdo hap të procesit!"',
        author: '- Gent, Durrës'
    }
];

let currentIndex = 0;
const testimonialText = document.getElementById('testimonial-text');
const testimonialAuthor = document.getElementById('testimonial-author');

function changeTestimonial() {
    currentIndex = (currentIndex + 1) % testimonials.length;
    testimonialText.style.opacity = 0;
    testimonialAuthor.style.opacity = 0;

    setTimeout(() => {
        testimonialText.textContent = testimonials[currentIndex].text;
        testimonialAuthor.textContent = testimonials[currentIndex].author;

        testimonialText.style.opacity = 1;
        testimonialAuthor.style.opacity = 1;
    }, 500); // Duration of fade-out
}

setInterval(changeTestimonial, 4000); // Change every 4 seconds
