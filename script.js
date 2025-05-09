const featureTabs = document.querySelectorAll(".feature-tab");
const featureImage = document.getElementById("feature-image");

const images = {
  payroll:
    "https://salient.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpayroll.517af4e7.png&w=1920&q=75",
  expenses:
    "https://salient.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fexpenses.3f331919.png&w=1920&q=75",
  vat: "https://salient.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fvat-returns.7402820f.png&w=1920&q=75",
  reporting:
    "https://salient.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freporting.2ad6f065.png&w=3840&q=75",
};

featureTabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    featureTabs.forEach((tab) => {
      tab.classList.remove(
        "bg-white/10",
        "backdrop-blur-sm",
        "border-2",
        "border-[#e5e7eb]/20",
        "border-r-none"
      );
    });

    tab.classList.add(
      "bg-white/10",
      "backdrop-blur-sm",
      "border-2",
      "border-[#e5e7eb]/20",
      "border-r-none"
    );

    featureImage.src = images[tab.id];
  });
});
const sectionImages = {
  reporting:
    "https://salient.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fprofit-loss.2a2f85d5.png&w=1920&q=75",
  inventory:
    "https://salient.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finventory.14ec7758.png&w=1920&q=75",
  contacts:
    "https://salient.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcontacts.a61dce95.png&w=1200&q=75",
};

const buttons = document.querySelectorAll('button[id$="-btn"]');
const dynamicFeatureImage = document.getElementById("dynamic-image");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    buttons.forEach((btn) => btn.classList.remove("bg-blue-700"));

    button.classList.add("bg-blue-700");

    const section = button.id.split("-")[0];

    if (sectionImages[section]) {
      dynamicFeatureImage.src = sectionImages[section];
    } else {
      console.error(`No image found for section: ${section}`);
    }
  });
});

const menuToggle = document.getElementById("menu-toggle");
const mobileMenu = document.getElementById("mobile-menu");

menuToggle.addEventListener("click", () => {

  mobileMenu.classList.toggle("hidden");
});