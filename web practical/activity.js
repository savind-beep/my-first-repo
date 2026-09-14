document.addEventListener("DOMContentLoaded", () => {
  // 1. Add Smooth Scrolling for all Links
  const links = document.querySelectorAll('a[href^="#"]');
  links.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const targetId = link.getAttribute("href");
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        targetElement.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // 2. Interactive Search Filter for the Nature Details Table
  const table = document.querySelector("table");
  if (table) {
    // Create search input field above table dynamically
    const searchInput = document.createElement("input");
    searchInput.type = "text";
    searchInput.placeholder = "Search table (e.g., Central, Elephants)...";
    searchInput.style.cssText = `
            width: 100%;
            max-width: 700px;
            padding: 10px 14px;
            margin-bottom: 15px;
            border: 1px solid #0b6637;
            border-radius: 6px;
            font-size: 0.95rem;
            box-sizing: border-box;
        `;

    table.parentNode.insertBefore(searchInput, table);

    // Filter table rows on typing
    searchInput.addEventListener("input", (e) => {
      const filterText = e.target.value.toLowerCase();
      const rows = table.querySelectorAll("tbody tr, tr:nth-child(n+2)");

      rows.forEach((row) => {
        const rowText = row.textContent.toLowerCase();
        if (rowText.includes(filterText)) {
          row.style.display = "";
        } else {
          row.style.display = "none";
        }
      });
    });
  }

  // 3. Image Click Zoom Modal Effect
  const images = document.querySelectorAll("img");
  images.forEach((img) => {
    img.style.cursor = "pointer";
    img.addEventListener("click", () => {
      const overlay = document.createElement("div");
      overlay.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(0, 0, 0, 0.85);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 1000;
                cursor: zoom-out;
            `;

      const fullImg = document.createElement("img");
      fullImg.src = img.src;
      fullImg.style.cssText = `
                max-width: 90%;
                max-height: 90%;
                border-radius: 8px;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
            `;

      overlay.appendChild(fullImg);
      document.body.appendChild(overlay);

      overlay.addEventListener("click", () => overlay.remove());
    });
  });
});
