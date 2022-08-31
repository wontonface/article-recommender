clickAndSelect()

function clickAndSelect() {
  let body-options = Array.from( document.querySelectorAll('.option-card-horizontal') ),
      elements = []
  
  // Add child nodes to clickable elements
  body-options.forEach(option-card-horizontal => {
    elements = elements.concat( Array.from(option-card-horizontal.children) )
  })

  // Attach to mouse events
  elements.forEach(element => {
    
    // click: Disable
    element.addEventListener('click', e => e.preventDefault())
    
    // mousedown: Log the timestamp
    element.addEventListener('mousedown', e => {
      let option-card-horizontal = e.target.closest(".option-card-horizontal")
      option-card-horizontal.setAttribute('data-md', Date.now())
    })
    
    // mouseup: Determine whether to click
    element.addEventListener('mouseup', e => {
      
      // Only one please
      e.stopPropagation();

      let option-card-horizontal = (e.target.classList.contains("option-card-horizontal")) ? e.target : e.target.closest('.option-card-horizontal'),
          then = option-card-horizontal.getAttribute('data-md'),
          now = Date.now()

      // Allow 200ms to distinguish click from non-click
      if(now - then < 200) {
        
        // Visit the link in the card
        // Change 'a' to a class if you have multiple links
        window.location = option-card-horizontal.querySelector('a').href
    
        // Remove for production
        option-card-horizontal.classList.add('visited')
        console.log(option-card-horizontal.querySelector('a').href)
        
      }
  
      // Clean up
      option-card-horizontal.removeAttribute('data-md')
      
    })
  })
}