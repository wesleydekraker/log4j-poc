package com.example.demo;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
class SampleController {
    private static final Logger logger = LogManager.getLogger(SampleController.class);

    @PostMapping("/login")
    String login(@RequestParam String username, @RequestParam String password) {
        logger.info("Username: " + username + " Password: " + password);
        return "Incorrect username/password. Your attempt will be logged!";
    }
}
