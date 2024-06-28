package com.api.crud.controllers;


import com.api.crud.models.UserModel;
import com.api.crud.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Optional;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/getUsers")
    public ArrayList<UserModel> getUsers(){
        return this.userService.getUser();
    }

    @PostMapping("/saveUser")
    public UserModel SaveUser(@RequestBody UserModel user){
        return this.userService.SaveUser(user);
    }

    @GetMapping(path = {"/{id}"})
    public Optional<UserModel> FindUserById(@PathVariable Long id){
        return this.userService.FindById(id);

    }

    @PutMapping(path = "/{id}")
    public UserModel UpdateById(@RequestBody UserModel request, Long id){
        return this.userService.UpdateById(request, id);
    }

    @DeleteMapping(path = "/{id}")
    public String DeleteById(@PathVariable("id") Long id){
        boolean ok = this.userService.DeleteUser(id);

        if (ok){
            return "User with ID: " + id +" delete with successfull.";

        }else{
            return "Error when you intented delete the user.";

        }

    }
}
