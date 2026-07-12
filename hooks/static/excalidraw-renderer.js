window.EXCALIDRAW_ASSET_PATH = "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/";
import { exportToSvg } from "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/dev/index.js";

class ExcalidrawRenderer extends HTMLElement {
  constructor() {
    super();
    const body = document.body;
    this.defaultColorTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? "dark" : "light";
    this.theme = body.getAttribute("data-md-color-media")
      ? "material"
      : "mkdocs";
    this.initTheme();
  }

  initTheme() {
    if (this.theme == "material") {
      const body = document.body;
      const isLightTheme =
        body.getAttribute("data-md-color-media") ===
        "(prefers-color-scheme: light)";
      this.mode = isLightTheme ? "light" : "dark";
      this.observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
          if (mutation.attributeName === "data-md-color-media") {
            if (body.getAttribute("data-md-color-media") === "(prefers-color-scheme: dark)" ) {
                this.mode = "dark";
            }
            else if (body.getAttribute("data-md-color-media") === "(prefers-color-scheme: light)" ) {
                this.mode = "light";
            }
            else {
                this.mode = this.defaultColorTheme;
            }
            this.connectedCallback();
          }
        });
      });
      this.observer.observe(body, { attributes: true , attributeFilter: ['data-md-color-media']});
    }
    if (this.theme == "mkdocs") {
      const doc = document.documentElement;
      const isLightTheme = doc.getAttribute("data-bs-theme") === "light";
      this.mode = isLightTheme ? "light" : "dark";
      this.observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
          if (mutation.attributeName === "data-bs-theme") {
            if (doc.getAttribute("data-bs-theme") === "dark" ) {
                this.mode = "dark";
            }
            else if (doc.getAttribute("data-bs-theme") === "light" ) {
                this.mode = "light";
            }
            this.connectedCallback();
          }
        });
      });
      this.observer.observe(document.documentElement, { attributes: true});
    }
  }

  handleTheme(data) {
    try {
      // 确保数据结构正确
      if (!data.appState) {
        data.appState = {};
      }
      data.appState.exportWithDarkMode = this.mode == "dark";
      data.appState.exportEmbedScene = true;
      data.exportPadding = 20;
      return data;
    } catch (e) {
      console.error("Error handling theme:", e);
      return data;
    }
  }

  async connectedCallback() {
    const src = this.getAttribute("src");
    if (!src) {
      this.showError("No source file specified");
      return;
    }

    try {
      const response = await fetch(src);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const contentType = response.headers.get("content-type");
      let data;
      
      try {
        const text = await response.text();
        data = JSON.parse(text);
      } catch (e) {
        console.error("Error parsing JSON:", e);
        throw new Error("Invalid Excalidraw file format");
      }

      // 验证数据结构
      if (!data || typeof data !== 'object') {
        throw new Error("Invalid Excalidraw data structure");
      }

      const svg = await exportToSvg(this.handleTheme(data));
      this.innerHTML = `<div style="display:flex;flex-direction: column;align-items: center"></div>`;
      const div = this.querySelector("div");
      div.appendChild(svg);
    } catch (e) {
      console.error("Error rendering Excalidraw:", e);
      this.showError(e.message || "Could not load diagram");
    }
  }

  showError(message) {
    this.innerHTML = `
      <div style="display:flex;flex-direction: column;align-items: center;color: #e74c3c;padding: 1em;">
        <p>Error: ${message}</p>
      </div>`;
  }

  disconnectedCallback() {
    if (this.observer) {
      this.observer.disconnect();
    }
  }
}

customElements.define("excalidraw-renderer", ExcalidrawRenderer);