// Code Tabs JavaScript for Just the Docs
// Add this to assets/js/code_tabs.js and include it in your layout

(function() {
  'use strict';

  const STORAGE_KEY = 'preferred-code-tab';

  // Initialize all tab groups on the page
  function initCodeTabs() {
    const tabGroups = document.querySelectorAll('.code-tabs');
    
    tabGroups.forEach(group => {
      const buttons = group.querySelectorAll('.code-tabs-btn');
      
      buttons.forEach(button => {
        button.addEventListener('click', () => {
          const tabName = button.dataset.tab;
          activateTab(group, tabName);
          syncTabs(tabName);
          savePreference(tabName);
        });

        // Keyboard navigation
        button.addEventListener('keydown', (e) => {
          handleKeyNavigation(e, buttons);
        });
      });
    });

    // Restore saved preference
    restorePreference();
  }

  // Activate a specific tab within a group
  function activateTab(group, tabName) {
    const buttons = group.querySelectorAll('.code-tabs-btn');
    const panels = group.querySelectorAll('.code-tabs-panel');

    buttons.forEach(btn => {
      const isActive = btn.dataset.tab === tabName;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-selected', isActive);
    });

    panels.forEach(panel => {
      const isActive = panel.dataset.tab === tabName;
      panel.classList.toggle('active', isActive);
      panel.hidden = !isActive;
    });
  }

  // Sync all tab groups on the page to the same language
  function syncTabs(tabName) {
    const allGroups = document.querySelectorAll('.code-tabs');
    
    allGroups.forEach(group => {
      // Check if this group has a tab with the selected name
      const matchingBtn = group.querySelector(`.code-tabs-btn[data-tab="${tabName}"]`);
      if (matchingBtn) {
        activateTab(group, tabName);
      }
    });
  }

  // Save preference to localStorage
  function savePreference(tabName) {
    try {
      localStorage.setItem(STORAGE_KEY, tabName);
    } catch (e) {
      // localStorage not available
    }
  }

  // Restore saved preference on page load
  function restorePreference() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        syncTabs(saved);
      }
    } catch (e) {
      // localStorage not available
    }
  }

  // Handle keyboard navigation (arrow keys)
  function handleKeyNavigation(event, buttons) {
    const buttonArray = Array.from(buttons);
    const currentIndex = buttonArray.indexOf(event.target);
    let newIndex;

    switch (event.key) {
      case 'ArrowLeft':
      case 'ArrowUp':
        event.preventDefault();
        newIndex = currentIndex - 1;
        if (newIndex < 0) newIndex = buttonArray.length - 1;
        buttonArray[newIndex].focus();
        buttonArray[newIndex].click();
        break;
      case 'ArrowRight':
      case 'ArrowDown':
        event.preventDefault();
        newIndex = currentIndex + 1;
        if (newIndex >= buttonArray.length) newIndex = 0;
        buttonArray[newIndex].focus();
        buttonArray[newIndex].click();
        break;
      case 'Home':
        event.preventDefault();
        buttonArray[0].focus();
        buttonArray[0].click();
        break;
      case 'End':
        event.preventDefault();
        buttonArray[buttonArray.length - 1].focus();
        buttonArray[buttonArray.length - 1].click();
        break;
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCodeTabs);
  } else {
    initCodeTabs();
  }
})();
